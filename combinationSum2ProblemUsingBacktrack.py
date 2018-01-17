class Solution(object):
    def combinationSum2(self, candidates, target):
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

        def constructCandidates(nums, combination):
            candidates = []
            visited = list(combination)
            for n in nums:
                if n not in visited:
                    candidates.append(n)
                else:
                    visited.remove(n)

            return candidates

        def processSolution(nums):
            print nums

        def backtrack(nums, target, combination):
            if sum(combination) > target:
                return

            #print combination

            if isSolution(combination, target):
                if combination not in result:
                    result.append(sorted(list(combination)))

            else:
                candidates = constructCandidates(nums, combination)
                for i in range(len(candidates)):
                    if i > 0 and candidates[i] == candidates[i - 1]:
                        continue
                    combination.append(candidates[i])
                    backtrack(nums, target, combination)
                    combination.pop()


        candidates = sorted(candidates)
        backtrack(candidates, target, [])
        import itertools
        result.sort()
        return list(k for k, _ in itertools.groupby(result))

s = Solution()
import time
start_time = time.time()
print s.combinationSum2([29,19,14,33,11,5,9,23,23,33,12,9,25,25,12,21,14,11,20,30,17,19,5,6,6,5,5,11,12,25,31,28,31,33,27,7,33,31,17,13,21,24,17,12,6,16,20,16,22,5],28)
print("--- %s seconds ---" % (time.time() - start_time))