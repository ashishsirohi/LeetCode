# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return
        if len(nums) == 1:
            return TreeNode(nums[0])

        mid = len(nums)/2
        left = list(nums[0:mid])
        right = list(nums[mid:len(nums)])

        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(left)
        root.right = self.sortedArrayToBST(right)

        return root


s = Solution()
nums = [-10,-3,0,5,9]
print s.sortedArrayToBST(nums)