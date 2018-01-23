class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
            return False
        self.memo = {}
        return self.AmIWinning(range(1, maxChoosableInteger + 1), desiredTotal)

    def AmIWinning(self, nums, desiredTotal):
        hash = str(nums)
        if hash in self.memo:
            return self.memo[hash]

        if nums[-1] >= desiredTotal:
            return True

        for i in range(len(nums)):
            if not self.AmIWinning(nums[:i] + nums[i + 1:], desiredTotal - nums[i]):
                self.memo[hash] = True
                return True
        self.memo[hash] = False
        return False

s = Solution()
print s.canIWin(18, 79)