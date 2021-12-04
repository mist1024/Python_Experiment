
# 转 2 进制
def toBin(num:int)->str:
    ans=""
    # 当 num 大于 0 时。
    while(num):
        # 位运算
        ans= ans+str(num&1)
        num >>= 1
    # 反转字符串
    return ans[::-1]


# 转 8 进制
def toOct(num: int) -> str:
    ans = ""
    while (num):
        ans+=str(num & 7)
        num >>= 3
    return ans[::-1]

# 转 16 进制
CONV = "0123456789abcdef"
def toHex(num: int) -> str:
    ans = []
    # 32位2进制数，转换成16进制 -> 4个一组，一共八组
    for _ in range(8):
        ans.append( CONV[num&15] )
        num >>= 4
        if not num:
            break
    return "".join(CONV[num] for n in ans[::-1])



if __name__ == '__main__':
    # 不能为负数。
    a=5
    print(toBin(a))
    print(toOct(a))
    print(toHex(a))
    print("十进制数为：", a)
    print("转换为二进制为：", bin(a))
    print("转换为八进制为：", oct(a))
    print("转换为十六进制为：", hex(a))