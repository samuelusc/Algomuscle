# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # a + b = b+a
        currentA, currentB = headA, headB

        while currentA != currentB:
            # It's crucial to understand why we can't use if currentA.next here
            # Using if currentA.next won't allow entering None, causing an infinite loop
            currentA = currentA.next if currentA else headB
            currentB = currentB.next if currentB else headA
        
        return currentA
 