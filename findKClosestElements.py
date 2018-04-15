class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        self.arr = arr
        self.x = x

        if x <= arr[0]:
            return arr[:k]

        if x >= arr[-1]:
            return arr[-k:]

        res = self.binarySearch(0, len(arr))

        if arr[res] == x:
            i = 0
            result = [x]
            currL = res - 1
            currR = res + 1
            while i < k - 1:
                if currL >= 0 and currR < len(arr) and abs(k - arr[currL]) <= abs(k - arr[currR]):
                    result.append(arr[currL])
                    currL -= 1
                    i += 1
                else:
                    print currR
                    result.append(arr[currR])
                    currR += 1
                    i += 1

            return sorted(result)
        else:
            pass

    def binarySearch(self, left, right):

        if left > right:
            return right

        mid = (left + right) / 2

        if self.arr[mid] == self.x:
            return mid

        if left == right:
            return left

        if self.arr[mid] > self.x:
            return self.binarySearch(left, mid - 1)
        else:
            return self.binarySearch(mid + 1, right)


ar = [1,2,3,4,5]
k = 4
x = 3
print Solution().findClosestElements(ar, k, x)