import collections
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need, missing = collections.Counter(t), len(t)
        left = 0
        right = 0
        i = 0
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1

            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not right or j - i <= right - left:
                    left, right = i, j

        return s[left:right]


S = "AADOBECODEBANC"
T = "ABC"
sol = Solution()
print sol.minWindow(S, T)
