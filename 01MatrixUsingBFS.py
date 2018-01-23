class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        import Queue
        myQueue = Queue.Queue()
        self.r = len(matrix)
        self.c = len(matrix[0])
        self.result = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        for i in range(self.r):
            for j in range(self.c):
                if matrix[i][j] == 0:
                    self.result[i][j] = 0
                    myQueue.put((i, j))
                else:
                    self.result[i][j] = float('inf')

        self.dfs(myQueue)
        return self.result

    def dfs(self, myQueue):
        while not myQueue.empty():
            currPos = myQueue.get()

            top = (currPos[0] - 1, currPos[1])
            bottom = (currPos[0] + 1, currPos[1])
            left = (currPos[0], currPos[1] - 1)
            right = (currPos[0], currPos[1] + 1)

            if top[0] >= 0 and top[0] < self.r and top[1] >= 0 and top[1] < self.c:
                if self.result[top[0]][top[1]] > 1 + self.result[currPos[0]][currPos[1]]:
                    self.result[top[0]][top[1]] = 1 + self.result[currPos[0]][currPos[1]]
                    myQueue.put(top)

            if bottom[0] >= 0 and bottom[0] < self.r and bottom[1] >= 0 and bottom[1] < self.c:
                if self.result[bottom[0]][bottom[1]] > 1 + self.result[currPos[0]][currPos[1]]:
                    self.result[bottom[0]][bottom[1]] = 1 + self.result[currPos[0]][currPos[1]]
                    myQueue.put(bottom)

            if left[0] >= 0 and left[0] < self.r and left[1] >= 0 and left[1] < self.c:
                if self.result[left[0]][left[1]] > 1 + self.result[currPos[0]][currPos[1]]:
                    self.result[left[0]][left[1]] = 1 + self.result[currPos[0]][currPos[1]]
                    myQueue.put(left)

            if right[0] >= 0 and right[0] < self.r and right[1] >= 0 and right[1] < self.c:
                if self.result[right[0]][right[1]] > 1 + self.result[currPos[0]][currPos[1]]:
                    self.result[right[0]][right[1]] = 1 + self.result[currPos[0]][currPos[1]]
                    myQueue.put(right)


s = Solution()
nums = [[0,0,0],[0,1,0],[1,1,1]]
print s.updateMatrix(nums)