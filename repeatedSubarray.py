def findLength(A, B):
    """
    :type A: List[int]
    :type B: List[int]
    :rtype: int
    """
    #memo = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
    dp = []
    for i in range(len(A)+1):
        x = [0] * (len(B)+1)
        dp.append(x)
    for i in range(len(A) - 1, -1, -1):
        for j in range(len(B) - 1, -1, -1):
            if A[i] == B[j]:
                dp[i][j] = dp[i + 1][j + 1] + 1
    return max(max(row) for row in dp)

    """if A == B:
        return len(A)
    l1 = len(A)
    l2 = len(B)
    i = 0
    maxlen = 0
    while i < l1:
        tmplen = 0
        tmp = i
        j = 0
        k = 0
        while j < l2:
            if tmp<l1 and A[tmp] == B[j]:
                j = j + 1
                tmp = tmp + 1
                tmplen += 1
            else:
                if tmplen > maxlen:
                    maxlen = tmplen
                j = k + 1
                k = j
                tmp = i
                tmplen = 0
        if tmplen > maxlen:
            maxlen = tmplen
        i = i + 1

    return maxlen"""


A=[1,2,3,2,1]
B=[3,2,1,4,7]
print findLength(A, B)