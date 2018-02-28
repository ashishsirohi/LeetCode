class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        self.myGraph = {}
        for i in range(len(graph)):
            self.myGraph[i] = graph[i]

        self.visited = set()
        for key, value in self.myGraph.iteritems():
            if key not in self.visited:
                res = self.bipartite(key)
                if not res:
                    return False

        return True

    def bipartite(self, node):
        import Queue
        myQueue = Queue.Queue()
        myQueue.put((node, 1))

        mySet1 = set()
        mySet2 = set()
        mySet1.add(node)
        self.visited.add(node)

        while not myQueue.empty():
            curr, st = myQueue.get()
            # print curr

            for edge in self.myGraph[curr]:
                if st == 1:
                    if edge in mySet1:
                        return False
                    else:
                        if edge not in mySet2 and edge not in self.visited:
                            self.visited.add(edge)
                            mySet2.add(edge)
                            myQueue.put((edge, 2))
                if st == 2:
                    if edge in mySet2:
                        return False
                    else:
                        if edge not in mySet1 and edge not in self.visited:
                            self.visited.add(edge)
                            mySet1.add(edge)
                            myQueue.put((edge, 1))

        return True


g = [[1, 2, 3],[0, 2],[0, 1, 3],[0, 2]]
s = Solution()
print s.isBipartite(g)