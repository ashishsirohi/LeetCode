import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        heapArr = []

        def pushPair(i, j):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(heapArr, [nums1[i] + nums2[j], i, j])

        pushPair(0, 0)
        result = []
        while heapArr and len(result) < k:
            currSum, i, j = heapq.heappop(heapArr)
            result.append([nums1[i], nums2[j]])
            pushPair(i, j + 1)
            if j == 0:
                pushPair(i + 1, 0)
        return result


n1 = [1,2,3]
n2 = [3,4,5]
k = 7
s = Solution()
print s.kSmallestPairs(n1, n2, k)