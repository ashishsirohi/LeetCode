class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        return self.binarySearch(nums, 0, len(nums) - 1, target)

    def binarySearch(self, nums, low, high, k):
        if low > high:
            return -1

        mid = (low + high) / 2

        if nums[mid] == k:
            return mid

        if nums[low] <= nums[mid]:
            if k >= nums[low] and k <= nums[mid]:
                return self.binarySearch(nums, low, mid - 1, k)
            else:
                return self.binarySearch(nums, mid + 1, high, k)

        if nums[mid] <= nums[high]:
            if k >= nums[mid] and k <= nums[high]:
                return self.binarySearch(nums, mid + 1, high, k)
            else:
                return self.binarySearch(nums, low, mid - 1, k)

        return -1

s = Solution()
print s.search([4,5,6,7,0,1,2], 4)