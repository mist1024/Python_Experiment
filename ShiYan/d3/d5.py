
def JieChen(num : int) -> int:
    if(num==0 | num==1):
        return 1
    return num * JieChen(num-1)



if __name__ == '__main__':
    while True:
        num=(int)(input("输入数字："))
        if(num>50):
            print("数字是不是太大了？")
        elif num<0:
            print("负数没有阶乘。程序终止")
            break
        else:
            print(num,"的阶乘是",JieChen(num))

        print("是否继续？输入一个负数终止 ！")