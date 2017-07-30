def insertionSort(arr):
    j = 1
    while j<len(arr):
        key = arr[j]
        i = j-1
        while i>=0 and arr[i]>key:
            arr[i+1] = arr[i]
            i = i - 1
        arr[i+1] = key
        j = j + 1

    print arr

def reverseInsertionSort(arr):
    j = 1
    while j < len(arr):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] < key:
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = key
        j = j + 1

    print arr

ll = [5, 2, 4, 6, 1, 3, 4, 11, 7, 8, 5, 12, 9]
insertionSort(ll)
reverseInsertionSort(ll)