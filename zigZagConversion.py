def zigZagconvert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    a = []
    for x in range(numRows):
        a.append("")
    i = 0
    x = 0
    while i < len(s):
        if x % numRows == 0 or x % numRows == numRows - 1:
            for j in range(numRows):
                if i < len(s):
                    a[j] = a[j] + s[i]
                    i = i + 1
        else:
            a[numRows - x % numRows - 1] = a[numRows- x % numRows - 1] + s[i]
            i = i + 1
        if x == numRows-1:
            x = 1
        else:
            x = x + 1

    out = ""
    for x in a:
        out = out + x

    return out


print zigZagconvert("abcdefghijk", 4)