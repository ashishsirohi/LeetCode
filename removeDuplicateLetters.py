class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        mydict = {}

        for c in s:
            try:
                mydict[c] += 1
            except KeyError:
                mydict[c] = 1

        print mydict
        res = []

        for c in s:
            if c not in res:
                while res and res[-1] > c:
                    count = mydict.get(res[-1])
                    if count:
                        res.pop()
                    else:
                        break

            if c not in res:
                res.append(c)
                mydict[c] -= 1
            else:
                mydict[c] -= 1

            print res
            print mydict

        return "".join(res)

s = "bcadhhgdbanndvbnvdvhgahdbvbvhjadv"

print Solution().removeDuplicateLetters(s)