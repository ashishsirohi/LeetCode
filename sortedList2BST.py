#Definition for singly - linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return
        if not head.next:
            return TreeNode(head.val)

        slow, fast = head, head.next.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        currNode = slow.next
        slow.next = None

        root = TreeNode(currNode.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(currNode.next)
        return root


nums = [-10,-3,0,5,9]
ll = ListNode(nums[0])
head = ll
for i in range(1,len(nums)):
    tmp = ListNode(nums[i])
    ll.next = tmp
    ll = ll.next

s = Solution()
print s.sortedListToBST(head)


