sum=0
n=int(input())
min=1000000
for i in range(0,n):
    x=int(input())
    if(x<min):
        min=x



if(min<0):
    temp=-1*min
else:
    temp=min

while(temp!=0):
    d=temp%10
    sum+=d
    temp=temp//10


if(min<0):
    sum=-1*sum

if(sum%2==0):
    print("1")
else:
    print("0")