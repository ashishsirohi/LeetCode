class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        result = []
        right = k
        left = 0
        while right < len(nums)+1:
            result.append(max(nums[left:right]))
            right += 1
            left += 1
        
        return result