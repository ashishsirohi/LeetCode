import Queue
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isValidString(s):
            count = 0
            for i in range(len(s)):
                c = s[i]
                if (c == '('):
                    count += 1
                if (c == ')'):
                    if (count == 0):
                        return False
                    count -= 1

            return count == 0

        result = []
        if isValidString(s):
            result.append(s)
            return result

        myQueue = Queue.Queue()
        visitedSet = set()
        myQueue.put(s)
        visitedSet.add(s)
        tmp = []
        minFlag = False
        while not myQueue.empty():
            currString = myQueue.get()


            if isValidString(currString):
                result.append(currString)
                minFlag = True
                l = len(currString)

            if minFlag:
                if l > len(currString):
                    break
                else:
                    continue

            removedChar = ""
            for i in range(len(currString)):
                if currString[i] != "(" and currString[i] != ")":
                    continue

                if currString[i] == removedChar:
                    continue

                if currString[i] == ")" and removedChar == "(":
                    removedChar = ""
                    continue
                tmpS = currString[:i]+currString[i+1:]
                removedChar = currString[i]
                if tmpS not in visitedSet:
                    tmp.append(tmpS)
                    visitedSet.add(tmpS)
                    myQueue.put(tmpS)

        return result


sol = Solution()
print sol.removeInvalidParentheses("(())))))()(()()x()(")