def findLuckyNumber(nums):
    # implement this function
    freq={} 
    for i in nums: 
        if(i not in freq): 
            freq[i]=1
        else: 
            freq[i]+=1 
    for i in nums:
        if(i==freq[i]): 
            return i
            
	
# DO NOT change anything below this line
if __name__ == "__main__":
    num_elems = int(input())
    input_arr = []
    for index in range(num_elems):
        input_arr.append(int(input()))
    x=findLuckyNumber(input_arr)
    print(x if(x) else -1)