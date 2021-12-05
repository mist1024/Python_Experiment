


def Upper(string: str):
    ans=""
    for i in range(len(string)):
        ans  += (int)(string[i]) | 31
    print(string)



if __name__ == '__main__':
    string = "fdsadfWEASDFA"
    # 库函数 位运算失败
    # Upper(string)

    print(string)
    print(string.lower())
    print(string.upper())