
# 更相减损术与辗转相除法 结合。
def gcd(a:int,b:int) ->int:
    if a==b:
        return a
    # 位运算判断奇偶性
    if a & 1 and b & 1:
        if a < b:
            a,b=b,a
        return gcd(a-b,b) # 更相减损术

    elif a&1 and b&1==0:
        return gcd(a,b>>1)

    elif a&1==0 and b&1:
        return gcd(a>>1 ,b)

    else:
        return gcd(a>>1,b>>1) <<1

if __name__ == '__main__':
    a=100
    b=60
    print(gcd(a,b))