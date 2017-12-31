class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if s == 0:
            return 0

        subarr = []
        left = 0
        right = 0
        maxSum = 0
        for i in range(len(nums)):
            maxSum += nums[i]

            if maxSum >= s:
                right = i
                subarr.append((left, right))
                while left < right:
                    maxSum -= nums[left]
                    if maxSum >= s:
                        left += 1
                        subarr.append((left, right))
                    else:
                        maxSum += nums[left]
                        break

        if len(subarr) > 0:
            return min([y-x for x, y in subarr]) + 1
        else:
            return 0


sol = Solution()
s = 0
nums = [5,1,3,5,10,7,4,9,2,8]
#s = 7
#nums = [2,3,1,2,4,3]
print sol.minSubArrayLen(s, nums)