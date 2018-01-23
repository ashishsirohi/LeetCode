class TreeNode(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None

class MyCalendar(object):

    def __init__(self):
        self.root = None

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        """if self.root is None:
            self.root = insertNode(self.root, TreeNode(start, end))
            return True"""
        
        return self.insertNode(self.root, TreeNode(start, end))
        
    def insertNode(self, root, node):
        if self.root is None:
            self.root = node
            return True
        
        if node.start >= root.end:
            if not root.right:
                root.right = node
                return True
            return self.insertNode(root.right, node)
        elif node.end <= root.start:
            if not root.left:
                root.left = node
                return True
            return self.insertNode(root.left, node)
        else:
            return False


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)