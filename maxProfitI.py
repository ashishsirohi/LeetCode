class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit, hold = 0, float('-inf')
        for i in range(len(prices)):
            profit = max(profit, hold + prices[i])
            hold = max(hold, - prices[i])
        return profit

s = Solution()
p = [7,1,5,3,6,4]
print s.maxProfit(p)