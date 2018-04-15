class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        # dp = [[0 for j in range(len(dungeon[0]) + 1)] for i in range(len(dungeon) + 1)]

        dp = []
        row1 = [float('inf')] * (len(dungeon) - 1)
        row1 += [0, float('inf')]
        for i in range(len(dungeon) - 1):
            tmp = list(dungeon[i])
            tmp.append(float('inf'))
            dp.append(tmp)

        dp.append(dungeon[-1] + [0])

        dp.append(row1)
        print dp

        for i in range(len(dungeon) - 1, -1, -1):
            for j in range(len(dungeon[0]) - 1, -1, -1):
                dp[i][j] = max(min(dp[i][j + 1], dp[i + 1][j]) - dungeon[i][j], 0)

        print dp



d = [[-2,-3,3],[-5,-10,1],[10,30,-5]]

print Solution().calculateMinimumHP(d)