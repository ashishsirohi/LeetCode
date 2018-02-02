class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        result = []
        graph = {}
        reverseGraph = {}
        independentSet = set(range(numCourses))
        for m, n in prerequisites:
            try:
                graph[n].append(m)
            except:
                graph[n] = [m]

            try:
                reverseGraph[m].append(n)
            except:
                reverseGraph[m] = [n]

            try:
                independentSet.remove(m)
            except:
                continue

        print graph
        while independentSet:
            curr = independentSet.pop()
            result.append(curr)

            if curr in graph.keys():
                for node in graph[curr]:
                    prerequisites.remove([node,curr])
                    reverseGraph[node].pop()
                    if reverseGraph[node] == []:
                        reverseGraph.pop(node, None)
                        independentSet.add(node)

        if prerequisites:
            return []

        return result


        print independentSet

s = Solution()
num = 4
pre = [[1,3],[2,0],[3,1],[3,2]]

print s.findOrder(num, pre)