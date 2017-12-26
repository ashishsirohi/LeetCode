def partition(s):
    """
    :type s: str
    :rtype: List[List[str]]
    """

    def dfs(s, path, result):
        if len(s) == 0:
            result.append(path)
            return
        for i in range(1, len(s) + 1):
            if isPalindrome(s[:i]):
                dfs(s[i:], path + [s[:i]], result)

    def isPalindrome(s):
        return s == s[::-1]

    result = []
    dfs(s, [], result)
    return result


s = "ababa"
print partition(s)