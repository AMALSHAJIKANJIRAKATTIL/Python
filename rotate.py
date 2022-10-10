from array import array


arr=input().split(" ")


for i in range(0,len(arr)):
    arr[i]=int(arr[i])


m=int(input())

for j in range(0,m):
    temp=arr[len(arr)-1]
    for i in range(len(arr)-2,-1,-1):
        arr[i+1]=arr[i]
    arr[0]=temp

for x in arr:
    print(x)