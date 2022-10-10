n=int(input())

spaces=n-1
stars=1

for i in range(1,2*n):
   
    for j in range(0,spaces):
        print(" ",end='')
    for x in range(0,stars):
        print("*",end="")
    if(i<n):
        spaces-=1
        stars+=2
    else:
        spaces+=1
        stars-=2
    print("")

