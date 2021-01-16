
def dao_chuoi(str):
    str_dao = str[::-1]
    return str_dao

def dao_nguoc_tu(str):
    str_dao_tu = ""
    for x in range(len(str.split(" "))-1,-1,-1):
        str_dao_tu = str_dao_tu + " " + str.split(" ")[x]
    return  str_dao_tu
if __name__ == '__main__':
    str = "abcdef"
    print(dao_chuoi(str))
    str2 = "abc def ghj 123 456"
    print(dao_nguoc_tu(str2))