# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverse(None, head)

    
    def reverse(self, pre: Optional[ListNode], cur: Optional[ListNode]) -> Optional[ListNode]:

        if not cur:
            return pre
        
        temp = cur.next
        cur.next = pre

        return self.reverse(cur, temp)
    