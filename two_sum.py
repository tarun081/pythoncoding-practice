#Two sum problem solution in python

nums = [2, 7, 11, 15]
target = 9
d = {}

for i in range(len(nums)):
        x = target - nums[i]

        if x in d:
            print([d[x], i])
            break
  
        d[nums[i]] = i
