m,n=map(int,input().split(" "))
arr=[]
sum=0
for i in range(0,m):
    arr.append(input().split(" "))

for i in range(0,m):
    for j in range(0,n):
        arr[i][j]=int(arr[i][j])
        if(arr[i][j]%2!=0):
            sum+=arr[i][j]
print(sum)