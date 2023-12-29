# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
            
        # Initialize the dummy node and the current node.
        dummy_node = ListNode()
        cur_node = head

        # Continously read the current node   
        while cur_node:
            # Save the link to the rest of the list in temp_next
            temp_next = cur_node.next

            # Isolate cur_node by pointing it to the beginning of the reversed list.            
            cur_node.next = dummy_node.next
            
            # Link the dummy node to the newly isolated node,
            dummy_node.next = cur_node
            
            # Move to the next node in the original list using the saved link.
            cur_node = temp_next
        
        return dummy_node.next