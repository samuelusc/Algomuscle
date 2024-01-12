# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 建立dummy 方便检查头节点
        dummy = ListNode(next = head)
        cur_node = dummy

        #需要有pre_node
        while cur_node.next:
            if cur_node.next.val == val:
                cur_node.next = cur_node.next.next

            # 保证next节点不是target
            else:
                cur_node = cur_node.next
        
        return dummy.next

                      
