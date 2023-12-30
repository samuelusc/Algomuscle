# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Check for boundary conditions: only one node or no nodes
        if not head or not head.next:
            return head
        dummy_node = ListNode(next = head)

        # cur_node to give the next pair's start
        # pre_node as the predecessor of the next head node
        cur_node, pre_node, stack = head, dummy_node, []

        # Need to consider two nodes at a time, so must include current node and current next node
        while cur_node and cur_node.next:
            
            _,_ = stack.append(cur_node),stack.append(cur_node.next)
            # Head of the next pair of nodes
            cur_node = cur_node.next.next

            # Use the stack's characteristics to sequentially connect to the dummy node
            pre_node.next = stack.pop()
            pre_node.next.next = stack.pop()

            # Move forward to the node that has been swapped, the node before the one to be added
            pre_node = pre_node.next.next
        
        # If the number of nodes is odd, connect the previous node with the remaining single node
        pre_node.next = cur_node if cur_node else None

        return dummy_node.next
