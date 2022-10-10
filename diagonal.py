n=int(input())
arr=[]
for i in range(0,n):
    arr.append(input().split(" "))

for i in range(0,n):
    for j in range(0,n):
        arr[i][j]=int(arr[i][j])
        if(i==j):
            if(arr[i][j]<0):
                arr[i][j]=0
            else:
                arr[i][j]=1
        print(arr[i][j], end=' ')
    print("")
