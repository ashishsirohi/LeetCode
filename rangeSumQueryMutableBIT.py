# Solution using Binary Indexed Tree - O(logn)
class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.length = len(nums) + 1
        self.tree = [0] + nums
        self.buildTree(nums)
        pass


    def buildTree(self, nums):
        for i in range(1, self.length):
            new_i = i + (i & -i)
            if new_i < self.length:
                self.tree[new_i] += self.tree[i]

        print self.tree
        pass

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        diff = val - self.nums[i]
        self.nums[i] = val
        i = i + 1
        while i < self.length:
            self.tree[i] += diff
            i += i & -i

        print self.tree

    def sumPrefix(self, i):
        """Computes prefix sum of up to including the i-th element"""
        i += 1
        result = 0
        while i:
            result += self.tree[i]
            i -= i & -i
        return result


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        """Computes the range sum between two indices (both inclusive)"""
        return self.sumPrefix(j) - self.sumPrefix(i - 1)

        pass



# Your NumArray object will be instantiated and called as such:
nums = [3,2,-1,6,5,4,-3,3,7,2,3]
obj = NumArray(nums)
obj.update(1,5)
param_1 = obj.sumPrefix(2)
print param_1
param_2 = obj.sumRange(0,2)
print param_2