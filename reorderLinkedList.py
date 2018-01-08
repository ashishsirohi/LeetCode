# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        #O(n2)
        """left = head
        while left.next:
            tmp = left
            if tmp.next.next:
                while tmp.next.next:
                    tmp = tmp.next if tmp else None

                tempNode = tmp.next
                tmp.next = None

                tempNode.next = left.next
                left.next = tempNode
                left = tempNode.next if tempNode else None
            else:
                break

        return head"""

        #Better Solution, O(n)
        if not head:
            return

        # find the mid point
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half in-place
        pre = None
        node = slow
        while node:
            pre, node.next, node = node, pre, node.next

        # Merge in-place; Note : the last node of "first" and "second" are the same
        first = head
        second = pre
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
        return

s = Solution()
ll = [1,2,3,4,5,6,7,8,9]
tmp = ListNode(ll[0])
head = tmp
for n in ll[1:]:
    node = ListNode(n)
    node.next = None
    tmp.next = node
    tmp = tmp.next

s.reorderList(head)
print head