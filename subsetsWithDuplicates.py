class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(nums, subset, start):
            print subset
            result.append(list(subset))

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                subset.append(nums[i])
                backtrack(nums, subset, i + 1)
                subset.pop()

        nums = sorted(nums)
        backtrack(nums, [], 0)
        return result

s = Solution()
import time
start_time = time.time()
print s.subsetsWithDup([1,2,2])
print("--- %s seconds ---" % (time.time() - start_time))
