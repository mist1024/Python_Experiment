
num=(int)(input("请输入数字："))

if num>0:
    print("num","是正数")
elif num<0:
    print("num","是负数")
else:
    print("num","是 0")


print("num",end=" ")
print("是正数") if num>0 else  print("是负数") if num<0 else print("是 0")