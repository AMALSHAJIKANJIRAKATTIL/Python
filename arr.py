arr=input().split(" ")
n=int(input())
bool=False
for i in arr :
    if(n==int(i)) :
        bool=True
        break

    
if(bool==True) :
    print("Found")
else :
    print("Not Found")