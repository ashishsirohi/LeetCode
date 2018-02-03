class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return []

        self.matrix = matrix
        self.l = len(matrix)
        self.b = len(matrix[0])
        dp1 = []
        for i in range(self.l):
            tmp = []
            for j in range(self.b):
                tmp.append(False)

            dp1.append(tmp)

        dp2 = []
        for i in range(self.l):
            tmp = []
            for j in range(self.b):
                tmp.append(False)

            dp2.append(tmp)

        for i in range(self.l):
            for j in range(self.b):
                if i == 0 or j == 0:
                    dp1[i][j] = True
                    continue

                if (matrix[i-1][j] <= matrix[i][j] and dp1[i-1][j] == True):
                    dp1[i][j] = True
                    continue

                if (matrix[i][j-1] <= matrix[i][j] and dp1[i][j-1] == True):
                    dp1[i][j] = True

        for i in range(self.l - 1, -1, -1):
            for j in range(self.b - 1, -1, -1):
                if i == self.l - 1 or j == self.b - 1:
                    dp2[i][j] = True
                    continue

                if (matrix[i+1][j] <= matrix[i][j] and dp2[i+1][j] == True):
                    dp2[i][j] = True
                    continue

                if (matrix[i][j+1] <= matrix[i][j] and dp2[i][j+1] == True):
                    dp2[i][j] = True

        print dp1
        print dp2
        result = []
        for i in range(self.l):
            for j in range(self.b):
                if dp1[i][j] == True and dp2[i][j] == True:
                    result.append([i,j])

        return result


        #return self.result


m = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
s = Solution()
print s.pacificAtlantic(m)