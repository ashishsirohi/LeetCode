def binarySearchRecursive(nums, k, left = 0, right = None):

    if right is None:
        right = len(nums) - 1

    if left > right:
        return "Not Found"

    mid  = left + right//2

    if not nums:
        return "Not Found"

    if k == nums[mid]:
        return mid
    elif k > nums[mid]:
        return binarySearchRecursive(nums, k, mid+1)
    else:
        return binarySearchRecursive(nums, k, 0, mid-1)

def binarySearchIterative(nums, k, left = 0, right = None):
    if right is None:
        right = len(nums) - 1

    if left > right:
        return "Not Found"

    while left <= right:
        mid  = left + right//2
        if k == nums[mid]:
            return mid
        elif k > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return "Not Found"



nums = [1,2]
print binarySearchRecursive(nums, 2)

print binarySearchIterative(nums, 0)