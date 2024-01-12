# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # two pointer 

        # 检查头节点不是空
        if not head:
            return None

        pre_node, cur_node = None, head

        while cur_node:
            #保留next节点信息
            temp = cur_node.next
            #再将current 指向 previous node
            cur_node.next = pre_node

            #pre 成为原来的cur_node
            pre_node = cur_node
            #再将保留的原next 赋给current
            cur_node = temp

        return pre_node

            
        