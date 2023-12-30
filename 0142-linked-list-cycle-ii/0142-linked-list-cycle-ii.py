# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize two pointers for the two-pointer technique.
        slow = fast = head
        # Move the fast pointer two steps and the slow pointer one step. 
        # If there's a cycle, they will meet.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # Once they meet, set another pointer at the start.
            if slow == fast:
                start = head
                # This pointer will meet the slow pointer at the start of the cycle.
                while start != slow:
                    start = start.next
                    slow = slow.next
                return start  # Cycle's entry point
        
        return None  # No cycle found
