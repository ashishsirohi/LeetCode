class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        self.visited = set()
        self.wordSet = set(wordDict)
        res = self.backtrack(s)
        return res


    def backtrack(self, s):
        if not s:
            return True

        for i in range(len(s)+1):
            curr = s[:i]
            if curr not in self.wordSet:
                continue
            else:
                if s[i:] not in self.visited:
                    self.visited.add(s[i:])
                    if self.backtrack(s[i:]):
                        return True
                    else:
                        continue
        return False

st = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
d = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

s = Solution()
print s.wordBreak(st, d)