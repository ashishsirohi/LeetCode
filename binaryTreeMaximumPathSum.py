# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        result = []

        def findMaxSum(root):

            if not root.left and not root.right:
                result.append((root.val, root.val))
                return (root.val, root.val)

            if root.left and not root.right:
                res = findMaxSum(root.left)[1]

                result.append((max(root.val, root.val + res),
                               max(root.val, root.val + res)))

                return (max(root.val, root.val + res),
                        max(root.val, root.val + res))

            if not root.left and root.right:
                res = findMaxSum(root.right)[1]

                result.append((max(root.val, root.val + res),
                               max(root.val, root.val + res)))

                return (max(root.val, root.val + res),
                        max(root.val, root.val + res))

            if root.left and root.right:
                res1 = findMaxSum(root.left)[1]
                res2 = findMaxSum(root.right)[1]

                result.append((max(root.val, root.val + res1 + res2, root.val + res1, root.val + res2),
                               max(root.val, root.val + max(res1, res2), root.val + res1, root.val + res2)))

                return (max(root.val, root.val + res1 + res2, root.val + res1, root.val + res2),
                        max(root.val, root.val + max(res1, res2), root.val + res1, root.val + res2))

        findMaxSum(root)
        print result

        return max(result, key=lambda item: item[0])[0]


nums = [1,2,3,4,55,6,7,8,10,-10,-20,4,2,1,3,2,4,2,3,-57,-56,-56,-57]
