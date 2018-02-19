def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    max_len = 0
    ll = []
    index = 1
    leng = 0
    x = 0

    while x < len(s):
        if s[x] not in ll:
            ll.append(s[x])
            x = x + 1
        else:
            if len(ll) >= max_len:
                max_len = len(ll)
            i = ll.index(s[x])
            del ll[0:i+1]
            ll.append(s[x])
            x = x + 1
            # index = index + 1

    if len(ll) > max_len:
        max_len = len(ll)

    return max_len


s = "pwwkew"
print lengthOfLongestSubstring(s)