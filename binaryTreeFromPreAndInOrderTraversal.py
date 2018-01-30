# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None

        root = TreeNode(preorder[0])

        leftIn = inorder[:inorder.index(root.val)]
        leftPre = preorder[preorder.index(root.val) + 1:preorder.index(root.val) + 1 + len(leftIn)]
        root.left = self.buildTree(leftPre, leftIn)

        rightIn = inorder[inorder.index(root.val) + 1:]
        rightPre = preorder[preorder.index(root.val) + 1 + len(leftIn):]
        root.right = self.buildTree(rightPre, rightIn)

        return root

preorder = [3,9,10,20,15,7]
inorder = [10,9,3,15,20,7]

s = Solution()
print s.buildTree(preorder, inorder)
