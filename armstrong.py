n=int(input())
temp=n
d=0
sum=0
if(temp<0):
    print("No")
else:
    while(temp!=0): 
        d=temp%10
        sum+=d*d*d
        temp=temp//10


    if(sum==n):
        print("Yes")
    else:
        print("No")