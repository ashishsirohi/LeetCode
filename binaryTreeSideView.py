# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        import Queue
        myQueue = Queue.Queue()
        myQueue.put(root)
        qList = [myQueue]
        result = []
        while qList:
            res, val = self.bfs(qList.pop())
            if val:
                result.append(val[-1])
            if not res.empty():
                qList.append(res)
        
        return result
        
    def bfs(self, queue):
        import Queue
        newQ = Queue.Queue()
        val = []
        while not queue.empty():
            curr = queue.get()
            val.append(curr.val)
            
            if curr.left:
                newQ.put(curr.left)
            if curr.right:
                newQ.put(curr.right)
        
        return newQ, val
            
        
