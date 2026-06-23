# Find max sub array/list sum of lenth K 

def find_sub_array_sum(l,k):
    sizeOflist = len(l)
    if sizeOflist == 0:
        return "is not possible as list is empty"
    if sizeOflist < k:
        return "is not possible as k is greater then list length"

    sum=0
    maxsum=0
    for i in range(0,k):
        sum=sum+l[i]
    maxsum=sum    
    for i in range(k,sizeOflist):
        sum = sum + l[i] - l[i-k]
        if sum > maxsum:
            maxsum=sum
    return maxsum     


l=[3,2,10,2,2,1]
x=find_sub_array_sum(l,4)
print(f"max sum in array {x}") 
