# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # if we don't use dummy node

        # Don't use if such as [7,7,7,7] target 7
        while head and head.val == val:
            head = head.next
                
        cur_node = head

        while cur_node and cur_node.next:
            if cur_node.next.val == val:
                cur_node.next = cur_node.next.next
            

            else:
                cur_node = cur_node.next
        
        return head
