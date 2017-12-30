class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        myStack = [-1]
        result = 0
        for i in range(len(s)):
            c = s[i]
            if c == "(":
                myStack.append(i)
            else:
                myStack.pop()
                if not myStack:
                    myStack.append(i)
                else:
                    result = max(result, i - myStack[-1])


        return result


s = Solution()
print s.longestValidParentheses("()()")