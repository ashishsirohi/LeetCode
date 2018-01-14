# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = ListNode(float('-inf'))

        while head:
            value = head.val
            tmp = node
            flag = False
            if not tmp.next:
                flag = True
                newNode = ListNode(value)
                tmp.next = newNode
            else:
                while tmp and tmp.next:
                    print tmp.val
                    if value > tmp.next.val:
                        tmp = tmp.next
                    else:
                        flag = True
                        newNode = ListNode(value)
                        newNode.next = tmp.next
                        tmp.next = newNode
                        break
            if not flag:
                newNode = ListNode(value)
                newNode.next = tmp.next
                tmp.next = newNode
            head = head.next
        return node.next


nums = [1,4,8,3,5,6,9,2]

head = ListNode(0)

tmp = head

for n in nums:
    newNode = ListNode(n)
    tmp.next = newNode
    tmp = tmp.next

s = Solution()
print s.insertionSortList(head.next)