n,k=map(int,input().split(" "))

if(n==0 or k ==0):
    print(0)

elif(n%k==0) :
    print(n%k)
else:
    print(((n//k)+1)-n//k)