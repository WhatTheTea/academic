nums = list(range(1,100+1))
length = len(nums)

def findMax(lst):
    max = 0
    for num in lst:
        if num > max:
            max = num
    return max


print("Before:\n", nums)

max = findMax(nums)
less20prc = []
toRemove = []
for i in range(len(nums)-1):
    if (max - nums[i]) < (max/100)*20:
        less20prc.append(nums[i])
        toRemove.append(nums[i])
for x in toRemove:
    nums.remove(x)
for x in nums:
    less20prc.append(x)



print("After \"sort\":\n", less20prc)