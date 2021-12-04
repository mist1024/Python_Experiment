import re


def s1(string :str):
    String = "[0-9]*"
    print(re.fullmatch(String, string))

def s2(string :str):
    String = "-[0-9]*"
    print(re.fullmatch(String, string))

def s3(string: str):
    String = "-?[0-9]*"
    print(re.fullmatch(String, string))

def s4(string: str):
    String='[A-Z]{26}'
    print(re.fullmatch(String,string))


def s5(string: str):
    String = "[a-z]{26}"
    print(re.fullmatch(String, string))


def s6(string: str):
    String = "([A-Z]|[a-z]){26}"
    print(re.fullmatch(String, string))


def s7(string: str):
    String="([A-Z]|[a-z]|[0-9]){26}"
    print(re.fullmatch(String,string))


def s8(string: str):
    String = re.compile("^[1-9]\\d{5}$")
    print(re.fullmatch(String, string))


def s9(string: str):
    String = re.compile("([0-9]{15}|[0-9]{18})")
    print(re.fullmatch(String, string))

if __name__ == '__main__':


    # 1
    string = '134123413241'
    s1(string)

    # 2
    string = '-13412341234'
    s2(string)

    # 3
    string = '-13421234'
    s3(string)


    # 4
    string = 'ASDFQWERTYUIOPGHJKLZXCVBNM'
    s4(string)

    # 5
    string = 'qwertyuiopasdfghjklzxcvbnm'
    s5(string)

    # 6
    string = 'qwertyuiASDFdfghjklzxcvbnm'
    s6(string)

    # 7
    string = 'qwerty12345Fdfgjklzxcvbjkl'
    s7(string)

    # 8
    string = '471400'
    s8(string)

    # 9
    string = '123411432324352'
    s9(string)
    print(len(string))