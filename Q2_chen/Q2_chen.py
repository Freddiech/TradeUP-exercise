
def reserse_string1(input):
    return " ".join(input.split(" ")[::-1])

def reserse_string2(input):
    string_list=input.split(" ")
    lp=0
    rp=len(string_list)-1
    while lp<rp:
        string_list[lp],string_list[rp]=string_list[rp],string_list[lp]
        lp+=1
        rp-=1
    return " ".join(string_list)

def reserse_string3(input):
    reversed_string=""
    while input:
        last_position=input.rfind(" ")
        word=input[last_position+1:]
        input=input[0:last_position]
        reversed_string+=word+" "
    return reversed_string[:-1]


if __name__ == '__main__':
    string='I love TradeUP'
    print(reserse_string1(string))
    print(reserse_string2(string))
    print(reserse_string3(string))
