class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        self.memo = {}
        path = []
        self.wordSet = set(wordDict)
        self.result = []
        self.tmp = []
        self.backtrack(s, path)
        return self.result
        #return res

    def backtrack(self, s, path):
        if s in self.memo:
            return self.memo[s]
        if not s:
            self.result.append(" ".join(path))
            return True

        for i in range(len(s) + 1):
            curr = s[:i]
            if curr not in self.wordSet:
                continue
            else:
                newpath = list(path)
                newpath.append(curr)
                if self.backtrack(s[i:], newpath):
                    continue
            self.memo[s] = " ".join(path)
st = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
d = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

st = "aaaaaaa"
d = ["aaa", "aaaa"]

st = "catsanddog"
d = ["cat", "cats", "and", "sand", "dog"]
s = Solution()
print s.wordBreak(st, d)