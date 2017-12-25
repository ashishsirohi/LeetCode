def minSubArrayLen(s, nums):
    """
    :type s: int
    :type nums: List[int]
    :rtype: int
    """
    subarr = []
    for i in range(len(nums)):
        tmp = nums[i]
        j = i+1
        s2 = tmp
        while j < len(nums) and s2 < s:
            s2 = s2 + nums[j]
            j = j+1
        if s2 >= s:
            subarr.append(j-i)
    #print subarr

    if len(subarr) > 0:
        return min(subarr)
    else:
        return 0

s = 1500
nums = [5,1,3,5,10,7,4,9,2,8]
print minSubArrayLen(s, nums)