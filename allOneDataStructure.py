class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.prev = None
        self.next = None
        

class AllOne(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.myds = {}
        self.minimax = collections.defaultdict(set)
        self.nodes = {}
        self.head = ListNode(None)
        self.tail = ListNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def insertNode_after(self, node, val):
        self.nodes[val] = ListNode(val) 
        newNode = self.nodes[val]
        newNode.next, newNode.prev = node.next, node
        node.next.prev = node.next = newNode
    
    def deleteNode(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
        node.next = node.prev = None
        self.nodes.pop(node.val)
        

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        # Incrementing the Key counter/setting it to 1
        self.myds[key] = self.myds.get(key, 0) + 1
        
        # Getting old and new values
        new, old = self.myds[key], self.myds[key] - 1
        
        # Getting current node from node dict, if doesn't exist or old == 0 then getting head node 
        current_node = old and self.nodes[old] or self.head
        
        # Updating Doubly Linked List
        if new not in self.nodes:
            self.insertNode_after(current_node, new)
        self.minimax[new].add(key)
        
        # Updating minimax dict
        if old:
            self.minimax[old].remove(key)
            self.update_minimax_old(old)
    
    def update_minimax_old(self, val):
        if not self.minimax[val]:
            self.deleteNode(self.nodes[val])
            self.minimax.pop(val)
    
    def isEmpty(self):
        return self.head.next == self.tail
        

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key in self.myds:
            old = self.myds[key]
            self.myds[key] -= 1
            new = self.myds[key]
            if not new:
                self.myds.pop(key)
            self.minimax[old].remove(key)
            if new:
                if new not in self.nodes:
                    self.insertNode_after(self.nodes[old].prev, new)
                self.minimax[new].add(key)
            self.update_minimax_old(old)
                
        

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        if self.isEmpty():
            return ""
        return next(iter(self.minimax[self.tail.prev.val]))
        

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        if self.isEmpty():
            return ""
        return next(iter(self.minimax[self.head.next.val]))
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
