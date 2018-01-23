class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return matrix

        r = len(matrix)
        c = len(matrix[0])
        result = [[float('inf') for i in range(len(matrix[0]))] for j in range(len(matrix))]
        # Pass 1, Top to Bottom
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    result[i][j] = 0
                else:
                    if i > 0:
                        result[i][j] = min(1 + result[i-1][j], result[i][j])
                    if j > 0:
                        result[i][j] = min(1 + result[i][j-1], result[i][j])


        # Pass 2, bottom to top
        for i in range(r-1, -1, -1):
            for j in range(c-1, -1, -1):
                if matrix[i][j] == 0:
                    result[i][j] = 0
                else:
                    if i < r:
                        result[i][j] = min(1 + result[i + 1][j], result[i][j])
                    if j < c:
                        result[i][j] = min(1 + result[i][j + 1], result[i][j])

        return result