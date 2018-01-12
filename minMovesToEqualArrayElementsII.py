# Using Quick-Select Algorihtm O(n) - Average Case (Similar to finding kth smallest element in unordered list, here k will be median)
from random import randint
class Solution(object):
    def __init__(self, nums):
        self.nums = nums

    def swap(self, i, j):
        temp = self.nums[i]
        self.nums[i] = self.nums[j]
        self.nums[j] = temp

    def partition(self, left, right, pivotIndex):
        pivotValue = self.nums[pivotIndex]

        self.swap(pivotIndex, right)
        storeIndex = left
        for i in range(left, right):
            if self.nums[i] < pivotValue:
                self.swap(storeIndex, i)
                storeIndex += 1
        self.swap(right, storeIndex)
        return storeIndex

    def select(self, left, right, k):
        if left == right:
            return self.nums[left]

        pivotIndex = randint(left, right)
        pivotIndex = self.partition(left, right, pivotIndex)
        if k == pivotIndex:
            return self.nums[k]
        elif k < pivotIndex:
            return self.select(left, pivotIndex - 1, k)
        else:
            return self.select(pivotIndex + 1, right, k)

    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        median = self.select(0, len(nums)-1, len(nums)/2)
        print median
        print nums
        moves = 0
        for i in range(len(self.nums)):
            moves += abs(median - self.nums[i])

        return moves


nums = [1,2,8,12,-13,56,11]
s = Solution(nums)
print s.minMoves2(nums)




