# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if head.next == None:
            return head

        odd = ListNode(0)
        even = ListNode(0)
        dummyOdd = odd
        dummyEven = even
        while head:
            odd.next = head
            odd = odd.next
            even.next = head.next
            even = even.next
            head = head.next.next if even else None

        odd.next = dummyEven.next

        return dummyOdd.next

s = Solution()
ll = [1,2,3,4,5,6,7,8]
tmp = ListNode(ll[0])
head = tmp
for n in ll[1:]:
    node = ListNode(n)
    node.next = None
    tmp.next = node
    tmp = tmp.next

print s.oddEvenList(head)