def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    l1 = len(nums1)
    l2 = len(nums2)
    if l1 >= l2:
        a1 = nums2
        a2 = nums1
    else:
        a1 = nums1
        a2 = nums2

    ll = []
    x = 0
    y = 0
    while x < len(a1):
        while y < len(a2):
            if a1[x] > a2[y]:
                ll.append(a2[y])
                y = y + 1
                if y == len(a2):
                    return x, a1, ll

            else:
                ll.append(a1[x])
                x = x + 1
                break
    return y, a2, ll

def main():
    arr1 = [1,2]
    arr2 = [1,2]
    combine_len = len(arr1) + len(arr2)
    x, arr, ll = findMedianSortedArrays(arr1, arr2)
    while x < len(arr):
        ll.append(arr[x])
        x = x + 1
    print ll
    #print combine_len
    if combine_len%2 == 0:
        print (ll[len(ll)/2] + ll[(len(ll)/2) - 1])/2.0
    else:
        print ll[((len(ll)+1)/2) - 1]

main()