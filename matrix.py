n,k=map(int,input().split(" "))
arr=input().split(" ")
count=0
for i in range(0,n) :
    arr[i]=int(arr[i])
    if(arr[i]==k):
        count+=1
print(count)