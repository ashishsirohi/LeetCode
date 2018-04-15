class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        if not s:
            return ""
        d.sort(key=lambda s: len(s), reverse=True)
        #target = set(list(s))
        result = []
        maxLen = 0
        for word in d:
            #curr = set(list(word))
            #if len(target.intersection(curr)) >= maxLen:
            res = self.lcs(s, word)
            if res == -1 and len(word) >= maxLen:
                maxLen = len(word)
                result.append(word)

        final = []
        for item in result:
            if len(item) == maxLen:
                final.append(item)

        #print final
        if final:
            final.sort()
            return final[0]

        return ""

    def lcs2(self, A, B):
        if len(A) == 0 or len(B) == 0:
            return 0

        if A[-1] == B[-1]:
            return 1 + self.lcs(A[:-1], B[:-1])
        else:
            return self.lcs(A[:-1], B)

    def lcs(self, A, B):
        j = len(B) - 1
        for i in range(len(A) - 1, -1, -1):
            if A[i] == B[j]:
                j -= 1

            if j == -1:
                break
        return j

s = "aaa"
l = ["aaa","aa","a"]

print Solution().findLongestWord(s, l)