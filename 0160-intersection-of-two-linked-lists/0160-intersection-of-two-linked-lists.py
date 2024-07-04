# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p_a,p_b = headA,headB

        while p_a != p_b:
            p_a = p_a.next if p_a else headB
            p_b = p_b.next if p_b else headA

        return p_a