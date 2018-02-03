class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return []

        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m = len(matrix)
        n = len(matrix[0])
        dp1 = [[False for _ in range(n)] for _ in range(m)]
        dp2 = [[False for _ in range(n)] for _ in range(m)]
        result = []

        for i in range(m):
            self.dfs(matrix, i, 0, dp1, m, n)
            self.dfs(matrix, i, n - 1, dp2, m, n)
        for j in range(n):
            self.dfs(matrix, 0, j, dp1, m, n)
            self.dfs(matrix, m - 1, j, dp2, m, n)

        for i in range(m):
            for j in range(n):
                if dp1[i][j] and dp2[i][j]:
                    result.append([i, j])
        return result

    def dfs(self, matrix, i, j, visited, m, n):
        visited[i][j] = True
        for dir in self.directions:
            x, y = i + dir[0], j + dir[1]
            if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] or matrix[x][y] < matrix[i][j]:
                continue
            self.dfs(matrix, x, y, visited, m, n)