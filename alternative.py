n=int(input())
sum=0
arr=input().split(" ")

for i in range(0,n,2):
    arr[i]=int(arr[i])
    sum+=arr[i]
print(sum)