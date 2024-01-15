# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        #将curret 指着 dummy
        cur_node = dummy
        
        #两两交换，至少要往前2次
        while cur_node.next and cur_node.next.next:
            #首先保存 第一个节点
            first_node = cur_node.next
            #保存第二个节点
            second_node = cur_node.next.next
           
            #将虚拟节点的下一个指向 第二个节点
            cur_node.next = second_node
            
            #将节点1的下一个指向节点2的下一个(1->3)
            first_node.next = second_node.next
            #将第节点2的下一个指向节点1（注意这里和上一个的顺序）
            second_node.next = first_node

            #把current指针移动到交换后的节点1
            cur_node = first_node
        
        return dummy.next