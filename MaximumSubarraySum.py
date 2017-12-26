def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return 0

    maxSum = nums[0]
    tmpSum = nums[0]

    for i in range(1, len(nums)):
        tmpSum = max(nums[i], (tmpSum + nums[i]))
        maxSum = max(maxSum, tmpSum)

    return maxSum

nums = [-2,1,-3,4,-1,2,1,-5,4,10]
print maxSubArray(nums)