# your code goes here
n,k=map(int,input().split(" "))

if((n+k)%12!=0):
    x=(n+k)%12
else:
    x=12
print(x)
