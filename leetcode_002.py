# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        out_list = ListNode(0)
        a = l1
        b = l2
        out = out_list
        up = 0
        while a and b:
            tmp = ListNode(0)
            tmp.val = (a.val+b.val+up)%10
            up = (a.val+b.val+up)//10
            out.next=tmp
            out=out.next
            a=a.next
            b=b.next
        if not a:
            while b:
                if up==1:
                    tmp = ListNode(0)
                    tmp.val = (b.val+up)%10
                    out.next=tmp
                    out=out.next
                    up = (b.val+up)//10
                    b = b.next
                else:
                    out.next = b
                    break
        else:
             while a:
                if up==1:
                    tmp = ListNode(0)
                    tmp.val = (a.val+up)%10
                    out.next=tmp
                    out=out.next
                    up = (a.val+up)//10
                    a = a.next
                else:
                    out.next = a
                    break
        if up==1:
            out.next=ListNode(1)
        return out_list.next