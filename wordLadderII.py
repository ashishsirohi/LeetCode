class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """

        def getSuccessor(word, WordList):
            successors = []
            for w in WordList:
                count = 0
                for i in range(len(word)):
                    if word[i] != w[i]:
                        count += 1
                if count == 1:
                    # yield w
                    successors.append(w)

            return successors

        result = []
        myStack = []
        import Queue
        state = (beginWord, [beginWord])
        # myStack.append(state)
        myQueue = Queue.Queue()
        myQueue.put(state)
        visited = []
        shortest = float('inf')
        while not myQueue.empty():
            # currWord, currPath = myStack.pop()
            currWord, currPath = myQueue.get()

            if currWord == endWord:
                if len(currPath) <= shortest:
                    result.append(currPath)
                    shortest = len(currPath)
                else:
                    break
                continue

            if len(currPath) > shortest:
                break

            """if currWord not in visited:
                visited.append(currWord)
            else:
                continue"""

            successors = getSuccessor(currWord, wordList)
            for s in successors:
                if s not in currPath:
                    # visited.append(s)
                    path = list(currPath)
                    path.append(s)
                    myQueue.put((s, path))
                    # myStack.append((s, path))

        return result


s = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog","cit","cot"]

print s.findLadders(beginWord, endWord, wordList)