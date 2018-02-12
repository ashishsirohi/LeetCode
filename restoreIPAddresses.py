class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.result = []
        self.dfs(s, 4, [])
        return [".".join(res) for res in self.result]

    def dfs(self, s, k, new_s):
        if len(s) > k * 3:
            return
        if k == 0:
            self.result.append(new_s)

        for i in range(min(3, len(s) - k + 1)):
            if i == 2 and int(s[:3]) > 255 or i > 0 and s[0] == '0':
                continue
            self.dfs(s[i + 1:], k - 1, new_s + [s[:i + 1]])

s =  Solution()
ip = "11111111111"
print s.restoreIpAddresses(ip)