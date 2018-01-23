# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        root = TreeNode(max(nums))
        index = nums.index(max(nums))
        leftsub = nums[:index]
        rightsub = nums[index + 1:]
        if leftsub:
            root.left = self.constructMaximumBinaryTree(leftsub)
        if rightsub:
            root.right = self.constructMaximumBinaryTree(rightsub)

        return root


n = [3,2,1,6,10,5,8,9,4]
s = Solution()
print s.constructMaximumBinaryTree(n)
