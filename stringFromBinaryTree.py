# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        result = ""
        path = str(t.val)
        myStack = [(t, path)]
        while len(myStack) > 0:
            currNode, currPath = myStack.pop()

            if currNode.left == None and currNode.right == None:
                tmpStr = "()()"
                currPath += tmpStr
                result += currPath
                continue

            if currNode.left != None:
                currPath += str(currNode.left.val)
                myStack.append((currNode.left, currPath))
            if currNode.right != None:
                currPath += str(currNode.right.val)
                myStack.append((currNode.right, currPath))

        return result

s = Solution()
print s.tree2str([1,2,3,4])