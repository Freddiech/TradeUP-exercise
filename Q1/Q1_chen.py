import pandas as pd
import re

def clean_format_phonenumber(input):
    # remove other characters except number
    input['PhoneNumber_cleaned'] = list(map(lambda phonenumber: re.sub(u"([^\u0030-\u0039])", "", phonenumber)
                                            , input['PhoneNumber']
                                            ))
    # validate phone number
    input['is_valid'] = list(map(lambda x: 1 if re.search("^[0-9]{10}$", x) else 0
                                , input['PhoneNumber_cleaned']
                                ))
    # format phone number
    input['output'] = list(map(lambda x, y: '-'.join(["({})".format(x[0:3]), x[3:6], x[6:10]]) if y == 1 else 'Not a Valid Phone Number'
                                ,input['PhoneNumber_cleaned']
                                , input['is_valid']
                                ))

    return input[['PhoneNumber','output']]

if __name__ == '__main__':
    """
    if input is a valid phone number(10 digit), reformat the phone number as (XXX)-XXX-XXXX
    if input is not a valid phone number, return 'Not a Valid Phone Number'
    """
    dataset = pd.read_csv("OA_DataCleaning.csv", header=0, encoding='UTF-8')
    result=clean_format_phonenumber(dataset)
    result.to_csv("Q1_chen.csv",header=True,index=False,encoding='UTF-8')
