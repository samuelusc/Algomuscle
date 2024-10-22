# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(start, end):
            pre,cur = None, start
            while cur != end:
                temp = cur.next
                cur.next = pre
                pre = cur
                cur = temp
            return pre
        
        dummy = ListNode(0,head)
        preTail = dummy
        while True:
            curTail = self.getKth(preTail, k)
            if not curTail:
                break
            nextHead = curTail.next
            originalHead = preTail.next
            reverseHead = reverse(originalHead, nextHead)
            preTail.next = reverseHead
            originalHead.next = nextHead
            preTail = originalHead
        
        return dummy.next
    
    def getKth(self, preTail, k):
        cur = preTail
        while cur and k > 0:
            cur = cur.next
            k -= 1
        return cur
            