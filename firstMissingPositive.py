def firstMissingPositive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    #Approach 1 - O(n) Space and Time
    """dict = {}
    for i in range(len(nums)+1):
        dict[i+1] = 0

    for i in range(len(nums)):
        if nums[i] in dict.keys():
            dict[nums[i]] += 1

    for i in range(len(nums)+1):
        if dict[i+1] == 0:
            return i+1"""

    #Approach 2 - O(1) Space O(n) Time
    for i in xrange(len(nums)):
        index = abs(nums[i]) - 1
        nums[index] = - abs(nums[index])

    return [i + 1 for i in range(len(nums)) if nums[i] > 0]

nums = [3,4,-1,1,2,5,7]
nums = [4,3,2,7,8,2,3,1]
print firstMissingPositive(nums)