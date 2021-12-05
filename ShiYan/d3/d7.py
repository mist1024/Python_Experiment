class OutNum(Exception):
    def __init__(self):
        print("数字有点大了")

def Flower():
    Num=(int)(input("输入一个整数"))
    if(Num>1000):
        raise OutNum()
    print(Num)
    for i in range(1,Num):
        m=i%10
        n=(int)((i/10)%10)
        j=(int)((i/100)%10)
        if(j*j*j+m*m*m+n*n*n==i):
            print(i,"是水仙花数")

if __name__ == '__main__':
    Flower()