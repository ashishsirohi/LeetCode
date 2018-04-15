class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxVal = nums[0]

        currmax = maxVal
        currmin = maxVal

        for n in nums[1:]:
            if n < 0:
                currmax, currmin = currmin, currmax

            currmax = max(n, currmax * n)
            currmin = min(n, currmin * n)

            maxVal = max(maxVal, currmax)

        return maxVal

nums = [2,3,-2,4,-2,-20]
print Solution().maxProduct(nums)