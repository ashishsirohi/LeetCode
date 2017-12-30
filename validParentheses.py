class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        myStack = [s[0]]
        for i in range(1, len(s)):
            c = s[i]
            if c == ")":
                if len(myStack) > 0:
                    if myStack[-1] == "(":
                        myStack.pop()
                    else:
                        myStack.append(c)
                else:
                    return False
            elif c == "}":
                if len(myStack) > 0:
                    if myStack[-1] == "{":
                        myStack.pop()
                    else:
                        myStack.append(c)
                else:
                    return False
            elif c == "]":
                if len(myStack) > 0:
                    if myStack[-1] == "[":
                        myStack.pop()
                    else:
                        myStack.append(c)
                else:
                    return False
            else:
                myStack.append(c)

        return len(myStack) == 0


s = Solution()
print s.isValid("(])")