from random import randint
class quickSort(object):
    def __init__(self, nums):
        self.nums = nums

    def swap(self, i, j):
        temp = self.nums[i]
        self.nums[i] = self.nums[j]
        self.nums[j] = temp

    def partiton(self, left, right, pivotIndex):
        pivotValue = self.nums[pivotIndex]

        self.swap(pivotIndex, right)

        tmpIndex = left
        for i in range(left, right):
            if self.nums[i] < pivotValue:
                self.swap(i, tmpIndex)
                tmpIndex += 1

        self.swap(tmpIndex, right)
        return tmpIndex

        pass

    def sort(self, left, right):
        if left < right:
            pivotIndex = randint(left, right)
            pivotIndex = self.partiton(left, right, pivotIndex)
            self.sort(left, pivotIndex-1)
            self.sort(pivotIndex+1, right)

nums = [1,4,6,2,0,8,11,9,16,17,13,-7,34,20,34,19]
q = quickSort(nums)
q.sort(0, len(nums)-1)
print q.nums
