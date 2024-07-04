# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                start_move = head
                intersect_move = fast

                while start_move != intersect_move:
                    start_move = start_move.next
                    intersect_move = intersect_move.next
                
                return start_move

        return  None
            