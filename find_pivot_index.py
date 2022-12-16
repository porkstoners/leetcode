nums = [1,7,3,6,5,6]

def pivotIndex(nums):
    total = sum(nums)
    leftSum = 0
    for i, x in enumerate(nums):
        if leftSum == (total - leftSum - x):
            return i
        leftSum +=x
    return -1

print(pivotIndex(nums))
