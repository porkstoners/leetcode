from rich import print as rprint

nums = [6, 3, 8, 5, 3]

def runningSum(nums):
    s=nums[0]
    for i in range(1,len(nums)):
        s=s+nums[i]
        nums[i]=s
    return nums
for x in runningSum(nums):
    rprint(f"The result is: {x}")
