n=int(input())
sum=0
prd=1
d=0
if(n==0) :
    print(0)
else :    
    while(n!=0) :
        d=n%10
        sum+=d
        prd*=d
        n=n//10
        
    print(prd-sum)