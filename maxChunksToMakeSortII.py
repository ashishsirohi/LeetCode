class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if not arr:
            return 0

        sortedArr = list(arr)
        sortedArr.sort()
        # print sortedArr

        maxArr = [arr[0]]
        for i in range(1, len(arr)):
            maxArr.append(max(maxArr[i - 1], arr[i]))

        # print maxArr

        count = 0
        upperLimit = float('inf')
        for i in range(len(arr) - 1, -1, -1):
            if maxArr[i] == sortedArr[i]:
                if sortedArr[i] > upperLimit:
                    continue
                count += 1
                upperLimit = arr[i]
        return count


n = [1,2,3,4,5,6,7,7,7,7,7,6,6,6]
s = Solution()
print s.maxChunksToSorted(n)