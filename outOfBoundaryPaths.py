class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        if N == 0:
            return 0
        if m == 0 or n == 0:
            return 0
        import Queue
        myQueue = Queue.Queue()
        state = ((i, j), [(i, j)])
        myQueue.put(state)
        count = 0
        while not myQueue.empty():
            currPos, currPath = myQueue.get()
            if currPos[0] < 0 or currPos[0] >= m or currPos[1] < 0 or currPos[1] >= n:
                count += 1
                continue

            if len(currPath) > N:
                continue

            child1 = (currPos[0] + 1, currPos[1])
            child2 = (currPos[0] - 1, currPos[1])
            child3 = (currPos[0], currPos[1] + 1)
            child4 = (currPos[0], currPos[1] - 1)

            newPath = list(currPath)
            newPath.append(child1)
            myQueue.put((child1, newPath))

            newPath = list(currPath)
            newPath.append(child2)
            myQueue.put((child2, newPath))

            newPath = list(currPath)
            newPath.append(child3)
            myQueue.put((child3, newPath))

            newPath = list(currPath)
            newPath.append(child4)
            myQueue.put((child4, newPath))

        return count