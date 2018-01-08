class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        # BFS Solution - TLE
        """if not p:
            return 0

        import Queue
        count = 0
        myQueue = Queue.Queue()
        visited = [p]
        myQueue.put(p)
        goal = "abcdefghijklmnopqrstuvwxyz"
        goal *= 10000

        while not myQueue.empty():
            currStr = myQueue.get()

            if currStr in goal:
                count += 1

            child1 = currStr[1:]
            child2 = currStr[:len(currStr) - 1]

            if child1 and child1 not in visited:
                visited.append(child1)
                myQueue.put(child1)
            if child2 and child2 not in visited:
                visited.append(child2)
                myQueue.put(child2)

        return count"""

        #DP Solution
        goal = "abcdefghijklmnopqrstuvwxyz"
        charDict = {}
        for i in range(len(goal)):
            charDict[goal[i]] = i

        maxLen = 0
        resultDict = {}
        for i in range(len(p)):
            if i > 0:
                if charDict[p[i]] - charDict[p[i-1]] == 1 or charDict[p[i-1]] - charDict[p[i]] == 25:
                    maxLen += 1
                else:
                    maxLen = 1
            else:
                maxLen = 1

            if p[i] in resultDict.keys():
                resultDict[p[i]] = max(resultDict[p[i]], maxLen)
            else:
                resultDict[p[i]] = maxLen

        #print resultDict
        result = 0
        for key, value in resultDict.iteritems():
            result += value

        return result

s = Solution()

p = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
#p = "zabab"
print s.findSubstringInWraproundString(p)