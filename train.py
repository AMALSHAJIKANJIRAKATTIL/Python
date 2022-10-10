n,p=map(int,input().split())
count=0

for j in range(n,0,-1) :
    count+=1
    if(j==p) :
        print(count)
        break
    