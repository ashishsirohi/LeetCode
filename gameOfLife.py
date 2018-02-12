class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        newb = []
        l = len(board)
        b = len(board[0])
        for i in range(l):
            tmp = []
            for j in range(b):
                tmp.append(0)
            newb.append(tmp)

        children = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
        for i in range(l):
            for j in range(b):
                numOnes = 0
                numZeros = 0
                for x, y in children:
                    px = i + x
                    py = j + y
                    if 0 <= px < l and 0 <= py < b:
                        if board[px][py] == 1:
                            numOnes += 1
                        else:
                            numZeros += 1
                print numOnes, numZeros
                if board[i][j] == 1:
                    if 2 <= numOnes <= 3:
                        newb[i][j] = 1
                    else:
                        newb[i][j] = 0
                else:
                    if numOnes == 3:
                        newb[i][j] = 1
                    else:
                        newb[i][j] = 0

        print newb
        for i in range(l):
            for j in range(b):
                board[i][j] = newb[i][j]

        print board

m = [[1],[0],[0],[1],[0],[0],[1],[0],[0],[1]]
s = Solution()
print s.gameOfLife(m)