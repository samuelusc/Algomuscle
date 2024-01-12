# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(pre_node, cur_node):
            #递归结束条件和返回值
            if not cur_node:
                # 需要返回反转的链表头部
                return pre_node

            temp_node = cur_node.next
            cur_node.next = pre_node
            
            # 单层递归逻辑
            # 需要有返回值
            return reverse(cur_node, temp_node)
        
        #递归参数
        return reverse(None, head)
