"""Won't work in case of duplicate string in the input list"""
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """

        def dfs(graph, node, mSum, nSum, m, n):
            count = 1
            state = (node, mSum, nSum, count)
            myStack = [state]
            visited = [node]
            while myStack:
                currNode, mSum, nSum, count = myStack.pop()
                visited.append(currNode)

                if mSum == m and nSum == n:
                    return count

                if mSum > m or nSum > n:
                    continue

                for t in graph:
                    if t not in visited and t not in markedParent:
                        childState = (t, mSum + t[0], nSum + t[1], count + 1)
                        myStack.append(childState)
            return 0

        List = []
        for s in strs:
            List.append((s.count("0"), s.count("1")))

        newList = sorted(List, key=sum, reverse=True)
        markedParent = []
        for i in range(len(newList) - 1, -1, -1):
            t = newList[i]
            if t not in markedParent:
                markedParent.append(t)
                mSum = t[0]
                nSum = t[1]
                res = dfs(newList, t, mSum, nSum, m, n)
                if res == 0:
                    continue
                else:
                    return res
        return 0



s = Solution()
l = ["10","0001","111001","1","0"]
m = 3
n = 4
print s.findMaxForm(l, m, n)