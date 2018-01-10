class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, list):
        self.tree = TreeNode(list[0])

    def buildTree(self, list):
        for i in range(1, len(list)):
            self.insertNode(self.tree, list[i])

        print self.tree

    def insertNode(self, tree, val):
        x = tree.val
        if val >= x:
            if not tree.right:
                newNode= TreeNode(val)
                tree.right = newNode
            else:
                self.insertNode(tree.right, val)
        else:
            if not tree.left:
                newNode= TreeNode(val)
                tree.left = newNode
            else:
                self.insertNode(tree.left, val)

    def searchNode(self, tree, val):
        if tree.val == val:
            return True

        if val > tree.val:
            if not tree.right:
                return False
            else:
                return self.searchNode(tree.right, val)
        else:
            if not tree.left:
                return False
            else:
                return self.searchNode(tree.left, val)

    def deletNode(self, tree, val):
        pass

    def inOrder(self, tree):
        if tree.left:
            self.inOrder(tree.left)
        print tree.val
        if tree.right:
            self.inOrder(tree.right)

    def preOrder(self, tree):
        print tree.val
        if tree.left:
            self.inOrder(tree.left)
        if tree.right:
            self.inOrder(tree.right)

    def postOrder(self, tree):
        if tree.left:
            self.inOrder(tree.left)
        if tree.right:
            self.inOrder(tree.right)
        print tree.val


tree = [8,3,5,10,11,6,13,17,2,9,4,12]
b = BST(tree)
b.buildTree(tree)
print b.searchNode(b.tree, 17)
print b.inOrder(b.tree)

