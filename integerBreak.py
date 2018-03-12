class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.dp = {1: 1}
        self.limit = n
        self.recursive(n)
        return self.dp[n]

    def recursive(self, n):
        if n > self.limit:
            return
        try:
            return self.dp[n]
        except KeyError:
            if n % 2 == 0:
                res = self.recursive(n / 2) ** 2
            else:
                res = self.recursive(n / 2) * self.recursive(n / 2 + 1)

            self.dp[n] = res

print Solution().integerBreak(10)