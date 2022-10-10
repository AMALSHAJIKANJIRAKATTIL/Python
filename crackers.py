n,k=map(int,input().split(" "))

rem=n%k
result=n//k

crackers=[0]*k

for i in range(0,k) :

    crackers[i]=result



for j in range(0,rem) :

    crackers[j]=crackers[j]+1
    rem-=1



answer=crackers[0]-crackers[k-1]
print(answer)