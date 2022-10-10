

m=int(input())
n=int(input())

if(m<0) :
    m=0
elif(n<0):
    n=0

if(m>n):
    print("-1")
else :    
    for i in range(m,n+1):
        print(i)