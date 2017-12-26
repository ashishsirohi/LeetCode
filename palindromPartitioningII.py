def minCut(s):
    """
    :type s: str
    :rtype: int
    """
    if s == s[::-1]:
        return 0

    for i in range(1, len(s)):
        if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
            return 1

    dp = [[0] * len(s) for i in range(len(s))]
    cut = range(len(s)) + [-1]
    for i in range(len(s)):
        for j in range(i, -1, -1):
            if s[i] == s[j] and (i - j < 2 or dp[i - 1][j + 1]):
                dp[i][j] = 1
                cut[i] = min(cut[i], cut[j - 1] + 1)
    return cut[-2]

s = "aabac"
print minCut(s)