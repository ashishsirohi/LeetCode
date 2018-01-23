# Definition for a binary tree node.
import copy
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        self.result = []
        roots = range(1, n + 1)
        rootDict = {}
        for i in range(len(roots)):
            self.node = TreeNode(roots[i])
            self.buildBST(self.node, roots[:i] + roots[i + 1:])
        return self.result

    def buildBST(self, node, nums):
        if not nums:
            return node
        for i in range(len(nums)):
            newNode = TreeNode(nums[i])
            newNums = list(nums)
            newNums.remove(nums[i])
            if nums[i] < node.val:
                node.left = self.buildBST(newNode, newNums)
            else:
                node.right = self.buildBST(newNode, newNums)

            if newNode.val == nums[i]:
                root_copy = copy.deepcopy(self.node)
                if node.val < root_copy.val:
                    root_copy.left = node
                else:
                    root_copy.right = node
                self.result.append(root_copy)


n = 3
s = Solution()
print s.generateTrees(n)