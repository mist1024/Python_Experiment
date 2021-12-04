
num = (int)(input("输入："))
m = num -1
arr=[]
for i in range(min(num,2)):
    arr.append(1)
for i in range(1 , m):
    arr.append(arr[i] + arr[i - 1])

print(arr)