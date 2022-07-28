import requests
from lxml import etree
import pandas as pd
import re

def data_extraction(url):
    #get data
    response = requests.get(url)
    #html to text
    response = etree.HTML(response.content.decode("utf-8"))
    response = response.xpath('/html/body/pre/text()')
    raw_text = " ".join(response).strip()
    #structure data
    data = raw_text.split("\r\n \r\n \r\n")
    data = list(map(lambda x: x.split("\r\n"), data))

    #data extraction
    res = pd.DataFrame(columns=['Code', 'Description', 'Open Interest'])
    for item in data:
        res.loc[res.shape[0]] = {
            'Code': re.findall('Code-[0-9a-zA-Z]{6}', item[0])[0]
            , 'Description': item[7].split("OPEN INTEREST:")[0].strip()
            , 'Open Interest': int(item[7].split("OPEN INTEREST:")[1].strip().replace(",", ""))
        }

    return raw_text,res

def write_txt(string,file_name):
    text_file = open("{}.txt".format(file_name), "w")
    text_file.write(string)
    text_file.close()

if __name__ == '__main__':
    url='https://www.cftc.gov/dea/futures/deanymesf.htm'
    raw_text,dataset=data_extraction(url)
    write_txt(raw_text,"raw_text_backup")
    dataset.to_csv("Q3_chen.csv",header=True,index=False,encoding='UTF-8')
