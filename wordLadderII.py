class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        def getSuccessor(word, wordSet):
            successors = []
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i + 1:]
                    if next_word in wordSet:
                        successors.append(next_word)
            return successors

        import Queue
        from collections import deque
        state = (beginWord, 1, [[beginWord]])
        path = deque()
        path.append(endWord)
        state2 = (endWord, 1, [path])
        myQueue = Queue.Queue()
        myQueue2 = Queue.Queue()
        myQueue.put(state)
        myQueue2.put(state2)
        shortest = float('inf')
        visitedDict = {}
        visitedDict2 = {}
        visitedDict[beginWord] = ([[beginWord]], 1)
        visitedDict2[endWord] = ([path], 1)
        result = set()
        while not myQueue.empty() and not myQueue2.empty():
            #print visitedDict
            currWord, length, currPath = myQueue.get()
            currWord2, length2, currPath2 = myQueue2.get()
            #print currWord

            try:
                val = visitedDict2[currWord][1]
                if length + val <= shortest:
                    shortest = length + val
                    result.add(tuple(currPath + list(visitedDict2[currWord][0])))

            except:
                pass

            try:
                val = visitedDict[currWord2][1]
                if length2 + val <= shortest:
                    shortest = length2 + val
                    result.add(tuple(visitedDict[currWord2][0] + list(currPath2)))

            except:
                pass

            if length < shortest:
                successors = getSuccessor(currWord, wordSet)
                for s in successors:
                    if s not in visitedDict:
                        try:
                            val = visitedDict2[s][1]
                            if length + val <= shortest:
                                shortest = length + val
                                for l in visitedDict2[s][0]:
                                    for m in currPath:
                                        result.add(tuple(m + list(l)))

                        except:
                            newP = []
                            for l in currPath:
                                newPath = list(l)
                                newPath.append(s)
                                newP.append(newPath)
                            visitedDict[s] = (newP, length + 1)
                            myQueue.put((s, length + 1, newP))
                            #print s
                    elif length + 1 <= visitedDict[s][1]:
                        newPath = list(currPath)
                        newPath.append(s)
                        visitedDict[s][0].append(newPath)
                        myQueue.put((s, length + 1, newPath))
                        # print s

            if length2 < shortest:
                successors = getSuccessor(currWord2, wordSet)
                for s in successors:
                    if s not in visitedDict2:
                        try:
                            val = visitedDict[s][1]
                            if length2 + val <= shortest:
                                shortest = length2 + val
                                for m in currPath2:
                                    for l in visitedDict[s][0]:
                                        result.add(tuple(l + list(m)))

                        except:
                            newP = []
                            for l in currPath2:
                                newPath = deque(l)
                                newPath.appendleft(s)
                                newP.append(newPath)
                            visitedDict2[s] = (newP, length2 + 1)
                            myQueue2.put((s, length2 + 1, newP))
                            # print visitedDict2
                    elif length2 + 1 <= visitedDict2[s][1]:
                        for l in currPath2:
                            newPath = deque(l)
                            newPath.appendleft(s)
                            visitedDict2[s][0].append(newPath)
                        # print visitedDict2


        if shortest == float('inf'):
            return []
        final = []
        for res in result:
            final.append(list(res))
        return final

s = Solution()
beginWord = "hot"
endWord = "dot"
wordList = ["hot","dot","dog"]

print s.findLadders(beginWord, endWord, wordList)