n=int(input())
arr=[]
for i in range(0,n):
    arr.append(int(input()))
m=int(input())

for i in range(0,m):
    for j in range(0,len(arr)//2):
        a=arr.pop()
        arr[j]=a+arr[j]
print(len(arr))

for i in arr:
    print(i)