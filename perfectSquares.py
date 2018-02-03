class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        total = 0
        import Queue
        myQueue = Queue.Queue()
        initSet = set()
        visited = set()
        while total < n:
            total = i**2
            initSet.add(i**2)
            myQueue.put((i**2, 1))
            visited.add(i**2)
            i += 1
        
        while not myQueue.empty():
            curr, length = myQueue.get()
            
            if curr == n:
                return length
            
            if curr > n:
                continue
            
            for num in initSet:
                if curr + num not in visited and curr + num <= n:
                    if curr + num == n:
                        return length + 1
                    visited.add(curr+num)
                    myQueue.put((curr + num, length + 1))
        
        return None
