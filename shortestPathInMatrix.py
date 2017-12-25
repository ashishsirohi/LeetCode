def findLength(A):
    """
    :type A: List[int]
    :type B: List[int]
    :rtype: int
    """
    dp = []
    for i in range(len(A)):
        x = [1] * (len(A))
        dp.append(x)
    for i in range(len(A) - 1, -1, -1):
        for j in range(len(A) - 1, -1, -1):
            if A[i][j] == 0:
                dp[i-1][j] = dp[i][j] + 1
                dp[i][j-1] = dp[i][j] + 1
                #dp[i-1][j-1] = dp[i][j] + 1
    print dp
    return max(max(row) for row in dp)

#A =[[0,0],[0,0]]
#A = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
A=[[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
findLength(A)