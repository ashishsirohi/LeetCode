import Queue
class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        def Successors(node):
            for i in xrange(4):
                x = int(node[i])
                for d in (-1, 1):
                    y = (x + d) % 10
                    yield node[:i] + str(y) + node[i + 1:]

        dead = set(deadends)
        myQueue = Queue.Queue()
        state = ('0000', 0)
        myQueue.put(state)
        visited = {'0000'}
        while not myQueue.empty():
            node, path = myQueue.get()
            if node == target: return path
            if node in dead: continue
            for successor in Successors(node):
                if successor not in visited:
                    visited.add(successor)
                    myQueue.put((successor, path + 1))
        return -1

s = Solution()
deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
print s.openLock(deadends, target)