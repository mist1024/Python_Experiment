
k = 0
for i in range(1,10):
    k=i+1
    for j in range(1,k):
        print( j ,'*', i , "=" , i*j ,end="\t")
    print()