class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Brute force - O(n2)
        """count = 0
        while len(set(nums)) > 1:
            skip = max(nums)
            flag = True
            for i in range(len(nums)):
                if nums[i] == skip and flag:
                    flag = False
                    continue
                else:
                    nums[i] += 1
            count += 1

        #print nums
        return count"""

        return sum(nums) - len(nums) * min(nums)

nums = [1,4,7,8,2,3,10,15,29,30,6]
s = Solution()
print s.minMoves(nums)