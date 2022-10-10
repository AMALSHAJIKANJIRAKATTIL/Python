# name you function as transpose_matrix and takes a list
# you should return a list of lists
def transpose_matrix(arr):
    lst=[]
    
    for i in range(0,len(arr[0])):
        sub=[]
        for j in range(0,h):
            
            sub.append(arr[j][i])
        lst.append(sub)
    return(lst)


# do not change anything below this line
if __name__ == "__main__":
    h = int(input())
    lst = []
    for val in range(0, h):
        lst.append([int(i) for i in input().split(' ')])
    out = transpose_matrix(lst)
    for val in out:
        print(" ".join(str(i) for i in val))