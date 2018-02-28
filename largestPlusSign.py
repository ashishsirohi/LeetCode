class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        self.mines = set()
        for l in mines:
            self.mines.add(tuple(l))

        print self.mines
        max = 0
        for i in range(N):
            for j in range(N):
                res = self.bfs(i, j, N)
                if res > max:
                    max = res
        return max

    def bfs(self, x, y, N):
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        import Queue
        myQueue = Queue.Queue()
        myQueue.put((x, y, (-1, -1), 1))
        visited = set()
        visited.add((x, y))
        max_count = 0
        while not myQueue.empty():
            x, y, d, count = myQueue.get()

            if count > max_count:
                max_count = count

            if d == (-1, -1):
                for i, j in directions:
                    new_x = x + i
                    new_y = y + j

                    if 0 <= new_x < N and 0 <= new_y < N and (new_x, new_y) not in self.mines and (
                    new_x, new_y) not in visited:
                        visited.add((new_x, new_y))
                        myQueue.put((new_x, new_y, (i, j), count + 1))
            else:
                new_x = x + d[0]
                new_y = y + d[1]

                if 0 <= new_x < N and 0 <= new_y < N and (new_x, new_y) not in self.mines and (
                new_x, new_y) not in visited:
                    visited.add((new_x, new_y))
                    myQueue.put((new_x, new_y, (d[0], d[1]), count + 1))

        return max_count

N = 5
m = [[4,2]]
print Solution().orderOfLargestPlusSign(N, m)