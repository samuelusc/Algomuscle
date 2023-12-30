# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Utilize a set to detect a cycle.
        # Sets can contain any hashable object, and ListNode can be inserted into a set.
        visited_nodes = set()

        # Traverse the linked list.
        while head:
            # If the node is already in the set, return it as the cycle's start node.
            if head in visited_nodes:
                return head
            # Add the current node to the set and move to the next node.
            visited_nodes.add(head)
            head = head.next
        # If no cycle is found, return None after complete traversal.
        return None
