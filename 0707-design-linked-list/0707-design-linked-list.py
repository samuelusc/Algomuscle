# 定义ListNode,leetcode已经包括这个可以直接用
# class ListNode:
#     def __init__(self, val = 0, next = None):
#         self.val = val
#         self.next = next

class MyLinkedList:

    def __init__(self):
        #添加dummy节点
        self.dummy = ListNode()
        #初始化size 为 0,这样新加就是从1开始
        self.size = 0


    def get(self, index: int) -> int:
        #检查index 边界
        if index < 0 or index >= self.size:
            return -1 

        #遍历链表
        #从head开始,也就是index 0 
        cur_node = self.dummy.next
        for _ in range(index):
            cur_node = cur_node.next
        
        #用 index = 0 测试    
        return cur_node.val

    def addAtHead(self, val: int) -> None:
        #重复利用已有函数
        #加头部元素也就是index 0 的元素，size 变成1
        self.addAtIndex(0,val)

    def addAtTail(self, val: int) -> None:
        #利用已有函数
        #链表添加元素从0开始,比如（0，1，2）
        #所以添加新的尾部则index 为 size = 3
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        #增加头部和尾部逻辑，放在这处理
        
        #首先处理边界,最大index
        #返回None 表示没有预期操作
        if index > self.size:
            return
        
        #找到previous_node
        pre_node = self.dummy
        for _ in range(index):
            pre_node = pre_node.next
        
        #新建节点,并让它指向当前 previous node 的next 节点（
        # 如果新节点是head,则previous 的下一个指向的None
        cur_node = ListNode(val, pre_node.next)
        # 然后将 pre_node 的下一个指向新建立的节点
        pre_node.next = cur_node
        
        ##注意要先把新节点指向原来的pre_node.next,保留关系
        ## 再把新节点设为pre_node.next
        
        #加完节点后记得size增长1
        self.size += 1
    def deleteAtIndex(self, index: int) -> None:
        #查看边界
        if index < 0 or index >= self.size:
            return 
        
        #遍历查找，定位到pre_node
        pre_node = self.dummy

        for _ in range(index):
            pre_node = pre_node.next
        
        #删除节点
        pre_node.next = pre_node.next.next
        #长度减1
        self.size -= 1



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)