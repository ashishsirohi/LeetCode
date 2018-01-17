class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []

        def isSolution(nums, n):
            if len(nums) == n:
                return True
            else:
                return False

        def constructCandidates(nums, inPerms):
            candidates = []
            for n in nums:
                if n not in inPerms:
                    candidates.append(n)
            return candidates

        def processSolution(nums):
            print nums

        def backtrack(nums, inPerms, j):
            print inPerms

            if isSolution(inPerms, len(nums)):
                #processSolution(inPerms)
                result.append(list(inPerms))
            else:
                candidates = constructCandidates(nums, inPerms)
                inPerms.append(0)
                for c in candidates:
                    inPerms[j] = c
                    backtrack(nums, inPerms, j+1)

                inPerms.pop()


        backtrack(nums, [], 0)
        return result


s = Solution()
import time
start_time = time.time()
print s.permute([1,2,3])
print("--- %s seconds ---" % (time.time() - start_time))



