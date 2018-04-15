class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        if not board[0]:
            return
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.globalvisited = set()
        self.l = len(board)
        self.b = len(board[0])
        self.board = board
        result = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "O" and (i, j) not in self.globalvisited:
                    self.globalvisited.add((i, j))
                    res = self.bfs(i, j)
                    result.append(res)

        print result
        for item in result:
            if len(item) > 0:
                for i, j in list(item):
                    board[i][j] = "X"

    def bfs(self, i, j):
        import Queue as Q
        myq = Q.Queue()
        visited = set([(i, j)])
        flag = False
        myq.put(((i, j), flag))

        while not myq.empty():
            curr, f = myq.get()

            for i, j in self.directions:
                new_i = curr[0] + i
                new_j = curr[1] + j

                if 0 <= new_i < self.l and 0 <= new_j < self.b:
                    if (new_i == 0 or new_i == self.l - 1 or new_j == 0 or new_j == self.b - 1) and self.board[new_i][
                        new_j] == "O":
                        flag = True
                    if (new_i, new_j) not in visited and (new_i, new_j) not in self.globalvisited and \
                                    self.board[new_i][new_j] == "O":
                        visited.add((new_i, new_j))
                        self.globalvisited.add((new_i, new_j))
                        flag = False
                        myq.put(((new_i, new_j), flag))
                else:
                    flag = True
                    break

        if flag:
            return set([])
        else:
            return visited


b = [["X","O","X","O","O","O","O"],["X","O","O","O","O","O","O"],["X","O","O","O","O","X","O"],["O","O","O","O","X","O","X"],["O","X","O","O","O","O","O"],["O","O","O","O","O","O","O"],["O","X","O","O","O","O","O"]]

print Solution().solve(b)