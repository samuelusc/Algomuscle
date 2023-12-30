# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy_node = ListNode(next = head)
        fast = slow = dummy_node
        
        # Move the fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next
        
        # Traverse with the fast pointer until the end
        # The slow pointer will reach the node just before the nth node from the end
        while fast.next:
            fast = fast.next
            slow = slow.next
            
        slow.next = slow.next.next
        return dummy_node.next
