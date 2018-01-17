class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        result = []

        def isSolution(nums, target):
            if sum(nums) == target:
                return True
            else:
                return False

        def constructCandidates(nums):
            candidates = []
            for n in nums:
                candidates.append(n)
            return candidates

        def processSolution(nums):
            print nums

        def backtrack(nums, target, combination, start):
            if sum(combination) > target:
                return

            #print combination

            if isSolution(combination, target):
                result.append(list(combination))

            else:
                #candidates = constructCandidates(nums)
                for i in range(start, len(candidates)):
                    combination.append(candidates[i])
                    backtrack(nums, target, combination, i)
                    combination.pop()

        candidates = sorted(candidates)
        backtrack(candidates, target, [], 0)
        import itertools
        result.sort()
        return list(k for k, _ in itertools.groupby(result))



s = Solution()
import time
start_time = time.time()
print s.combinationSum([8,6,4,12,5,7,3,11], 28)
print("--- %s seconds ---" % (time.time() - start_time))



