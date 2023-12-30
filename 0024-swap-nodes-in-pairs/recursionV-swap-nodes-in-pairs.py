# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Check for edge cases and establish the base case for recursion
        if not head or not head.next:
            return head

        new_head = head.next
        head.next = self.swapPairs(new_head.next)
        
        # Connect the new head node to the original head
        new_head.next = head
        
        # Return the new head (both for recursion backtracking and as the final output)
        return new_head
