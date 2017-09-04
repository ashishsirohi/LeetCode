def longestPalindrome(s):
    if len(s) == 1:
        return s
    if len(s) == 2:
        if s[0] == s[1]:
            return s
        else:
            return s[0]
    c = 0
    for x in s:
        if s[0] == x:
            c = c + 1
        else:
            break
    if c == len(s):
        return s
    k = 1
    ll = []
    res = ""
    while k < len(s):
        ll.append(res)
        res = s[k]
        i = k - 1
        j = k + 1
        f = 0
        while i>=0 and j<len(s):
            if s[i] == s [j]:
                res = s[i] + res + s[j]
                i = i - 1
                j = j + 1
                f = 1
            elif s[k] == s[j] and f == 0:
                res = res + s[j]
                j = j + 1
            elif s[k] == s[i] and f == 0:
                res = res + s[i]
                i = i - 1
            else:
                break
        k = k + 1

    max = 0
    out = ""
    for x in ll:
        if len(x) > max:
            max = len(x)
            out = x
    return out

print longestPalindrome("aaaa")