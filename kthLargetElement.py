class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        self.nums = nums
        for i in range(len(self.nums) / 2, -1, -1):
            self.maxHeapify(i)

        print self.nums
        i = 0
        while i < k:
            self.nums[0], self.nums[-1] = self.nums[-1], self.nums[0]
            result = self.nums.pop()
            self.maxHeapify(0)
            i += 1

        return result

    def maxHeapify(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index
        if left < len(self.nums) and self.nums[left] > self.nums[largest]:
            largest = left
        if right < len(self.nums) and self.nums[right] > self.nums[largest]:
            largest = right
        if largest != index:
            self.nums[index], self.nums[largest] = self.nums[largest], self.nums[index]
            self.maxHeapify(largest)
