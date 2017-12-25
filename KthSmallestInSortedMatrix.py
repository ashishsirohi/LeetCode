def kthSmallest(matrix, n):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    if n == 1:
        return matrix[0][0]
    i = 0
    j = 0
    k = 0
    l = 0
    ll = []
    print matrix[i][j]
    while i < len(matrix) or l < len(matrix):
        j = i
        k = l
        ll.append(matrix[i][j])
        while j < len(matrix) - i - 1 and k < len(matrix) - l - 1:
            if matrix[i][j + 1] <= matrix[k + 1][l]:
                ll.append(matrix[i][j + 1])
                j += 1
            else:
                ll.append(matrix[k + 1][l])
                k += 1

        while j!=len(matrix) - i - 1:
            ll.append(matrix[i][j + 1])
            j += 1

        while k!=len(matrix) - l - 1:
            ll.append(matrix[k + 1][l])
            k += 1

        if len(ll) == n:
            break
        else:
            i += 1
            l += 1

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 4
print kthSmallest(matrix, k)