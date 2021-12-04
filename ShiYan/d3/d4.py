def RunNian(num):
    print(num, "是闰年")


def FeiRunNian(num):
    print(num, "不是闰年")

num=(int)(input("输入年份："))

if num&3==0:
    if(num%100==0):
        if(num%400 ==0):
            RunNian(num)
        else:
            FeiRunNian(num)
    else:
        RunNian(num)
else:
    FeiRunNian(num)
