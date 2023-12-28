# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappop, heappush
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        heap = []
        count = 0

        for link in lists:
            if link:
                heappush(heap,(link.val, count, link))
                count += 1
        
        while heap:
            val, count, node = heappop(heap)
            current.next = node
            current = current.next

            if node.next:
                heappush(heap,(node.next.val, count, node.next))
                count += 1


        return dummy.next

