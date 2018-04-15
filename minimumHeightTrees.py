class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        mygraph = {}

        for edge in edges:
            try:
                mygraph[edge[0]].append(edge[1])
            except KeyError:
                mygraph[edge[0]] = [edge[1]]

            try:
                mygraph[edge[1]].append(edge[0])
            except KeyError:
                mygraph[edge[1]] = [edge[0]]

        self.mygraph = mygraph
        self.dp = {}
        for key, value in mygraph.iteritems():
            visited = set([key])
            self.dfs(key, visited)

        print self.dp

        minVal = float('inf')
        for key, value in self.dp.iteritems():
            if value < minVal:
                minVal = value

        result = []
        for key, value in self.dp.iteritems():
            if value == minVal:
                result.append(key)

        return result

    def bfs(self, node):
        import Queue as Q
        myq = Q.Queue()
        visited = set([node])
        myq.put((node, 0))
        try:
            self.dp[node]
        except:
            self.dp[node] = 0

        while not myq.empty():
            curr, path = myq.get()

            for nodes in self.mygraph[curr]:
                if nodes not in visited:
                    try:
                        old = self.dp[nodes]
                        self.dp[nodes] = max(old, path + old)
                    except:
                        self.dp[nodes] = path + 1

                    visited.add(nodes)
                    myq.put((nodes, path + 1))

        return

    def dfs(self, node, visited):
        for item in self.mygraph[node]:
            if item not in visited:
                visited.add(item)
                self.dfs(item, visited)
                try:
                    self.dp[node] = max(self.dp[node], 1 + self.dp[item])
                except KeyError:
                    self.dp[node] = 1 + self.dp[item]

        self.dp[node] = self.dp.get(node, 0)
        return


n = 6
edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

print Solution().findMinHeightTrees(n, edges)