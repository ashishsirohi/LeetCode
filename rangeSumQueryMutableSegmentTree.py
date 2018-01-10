# Solution using Segment Tree - O(logn)
class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.l = len(nums)
        self.tree = [0]*self.l*2
        self.buildTree(nums)
        print self.tree

    def buildTree(self, nums):
        j = 0
        for i in range(self.l, self.l*2):
            self.tree[i] = nums[j]
            j += 1

        for i in range(self.l-1, -1, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        i += self.l
        self.tree[i] = val
        while i > 0:
            left = i
            right = i
            if (i % 2 == 0):
                right = i + 1
            else:
                left = i - 1
        # parent is updated after child is updated
            self.tree[i / 2] = self.tree[left] + self.tree[right]
            i /= 2

        print self.tree


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        # get leaf with value 'l'
        i += self.l
        # get leaf with value 'r'
        j += self.l
        result = 0
        while i <= j:
            if (i % 2) == 1:
                result += self.tree[i]
                i += 1
            if ((j % 2) == 0):
                result += self.tree[j]
                j -= 1
            i /= 2
            j /= 2
        return result



# Your NumArray object will be instantiated and called as such:
nums = [2,4,5,7,8,9]
obj = NumArray(nums)
#obj.update(0,3)
param_2 = obj.sumRange(0,2)
print param_2