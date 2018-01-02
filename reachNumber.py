class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        import Queue
        myQueue = Queue.Queue()
        state = (0, 0)
        myQueue.put(state)
        while not myQueue.empty():
            currNode, currPath = myQueue.get()

            if currNode == target:
                return currPath

            else:
                child1 = currNode + (currPath + 1)
                child2 = currNode - (currPath + 1)
                myQueue.put((child1, currPath + 1))
                myQueue.put((child2, currPath + 1))


s = Solution()
print s.reachNumber(-1000000000)

