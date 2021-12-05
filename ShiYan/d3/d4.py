def RunNian(num):
    print(num, "是闰年")


def FeiRunNian(num):
    print(num, "不是闰年")

num=(int)(input("输入年份："))

if num&3==0:
    FeiRunNian(num)
else:
    if (num % 100):
        RunNian(num)
    else:
        if (num % 400):
            FeiRunNian(num)
        else:
            RunNian(num)
