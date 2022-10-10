n=int(input())
arr=[]

for i in range(0,n):
    arr.append(input().split(" "))

for i in range(0,len(arr[0])):
    for j in range(0,n):
        arr[j][i]=int(arr[j][i])
        print(arr[j][i],end=' ')
    print("")

