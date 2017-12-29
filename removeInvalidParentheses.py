class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isValidString(s):
            i = 0
            myStack = []
            while i < len(s):
                if s[i] == ")" and len(myStack)>0:
                    if myStack[-1] == "(":
                        myStack.pop()
                    else:
                        myStack.append(s[i])
                elif s[i] == "(" or s[i] == ")":
                    myStack.append(s[i])

                i += 1
            if len(myStack) == 0:
                return True
            else:
                return False

        result = []
        if isValidString(s):
            result.append(s)
            return result

        counter = 0
        for i in range(len(s)):
            if s[i] == "(":
                counter += 1
            elif s[i] == ")":
                counter -= 1

        if counter < 0:
            s_copy = s
            for i in range(len(s_copy)):
                if s_copy[i] == ")":
                    tmpS = s_copy[:i]+s_copy[i+1:]
                    if tmpS not in result and isValidString(tmpS):
                        result.append(tmpS)
        if counter > 0:
            s_copy = s
            for i in range(len(s_copy)):
                if s_copy[i] == "(":
                    tmpS = s_copy[:i] + s_copy[i + 1:]
                    if tmpS not in result and isValidString(tmpS):
                        result.append(tmpS)

        if len(result) == 0 and not isValidString(s):
            res = s.replace("(", "")
            result.append(res.replace(")", ""))

        return result


sol = Solution()
print sol.removeInvalidParentheses(")()(")