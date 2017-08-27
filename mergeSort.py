import math

def mergeSort(arr, p, r):
    if p<r:
        q = math.floor((p+r)/2)
        mergeSort(arr, p, q)
        mergeSort(arr, q+1, r)
        merge(arr, p, q, r)

def merge(arr, p, q, r):
    n1 = int(q-p+1)
    n2 = int(r-q)
    i = int(p)
    j = int(q)
    L = []
    R = []
    for x in range(n1):
        L.append(arr[i])
        i = i + 1
    for x in range(n2):
        R.append(arr[j+1])
        j = j +1

    i = 0
    j = 0
    res = []
    while i<n1 and j<n2:
        if L[i] <= R[j]:
            res.append(L[i])
            i = i+1
        else:
            res.append(R[j])
            j = j+1

    if i != n1:
        while i<n1:
            res.append(L[i])
            i += 1

    if j != n2:
        while j<n2:
            res.append(R[j])
            j += 1
    i = 0
    while p<=r:
        arr[int(p)] = res[i]
        i = i +1
        p = p +1

    print arr

mergeSort([23, 56, 12, 46, 34, 76, 39], 0, 6)
#merge([23, 24, 28, 34, 12, 26, 46, 76], 0, 3, 7)