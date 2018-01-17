class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        result = []

        def isSolution(nums, n, k):
            if len(nums) == n:
                return True
            else:
                return False

        def constructCandidates():
            return [1, 0]

        def processSolution(nums):
            print nums

        def backtrack(nums, n, k, j):

            if nums and len(nums) >= k:
                if nums.count(0) > n-k or nums.count(1) > k:
                    return

            #print nums

            if isSolution(nums, n, k):
                # processSolution(nums)
                if nums.count(1) == k:
                    tmp = []
                    j = 1
                    for n in nums:
                        if n == 1:
                            tmp.append(j)
                        j += 1
                    result.append(tmp)

            else:
                candidates = constructCandidates()
                nums.append(0)
                for c in candidates:
                    nums[j] = c
                    backtrack(nums, n, k, j + 1)

                nums.pop()

        backtrack([], n, k, 0)
        return result


s = Solution()
n = 20
k = 16
import time
start_time = time.time()
print s.combine(n,k)
print("--- %s seconds ---" % (time.time() - start_time))



