# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        p = res
        c = 0
        while (l1 or l2):
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum = (x + y + c) % 10
            c = (x + y + c) // 10
            p.next = ListNode(sum)
            p = p.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        if (c > 0):
            p.next = ListNode(1)
        return res.next



