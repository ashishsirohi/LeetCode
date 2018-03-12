class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        self.mygraph = {}

        for i in range(len(graph)):
            self.mygraph[i] = graph[i]

        print self.mygraph
        self.target = i
        print self.target
        self.result = []
        self.dfs(0, [0])
        print self.result

    def dfs(self, node, path):
        if node == self.target:
            self.result.append(path)
            return

        for child in self.mygraph[node]:
            newpath = list(path)
            newpath.append(child)
            self.dfs(child, newpath)


print Solution().allPathsSourceTarget([[1,2],[3],[3],[]])