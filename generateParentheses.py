class Solution(object):
    def generateParenthesis(self, n):
        def generate(A = []):
            if len(A) == 2*n:
                if isValidString(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

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

        ans = []
        generate()
        return ans

s = Solution()
print s.generateParenthesis(3)