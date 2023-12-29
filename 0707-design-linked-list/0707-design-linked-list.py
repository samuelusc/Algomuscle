# Build myself but not necessary in leetcode
# class ListNode:
#     def __init__(self, val=0,next= None):
#         self.val = val
#         self.next = next

class MyLinkedList:

    def __init__(self):
        self.dummy_node = ListNode()
        self.size  = 0    

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        cur_node = self.dummy_node.next
        
        for _ in range(index):
            cur_node = cur_node.next
        return cur_node.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)
 
    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)


    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
             return
        
        predecessor = self.dummy_node
        for _ in range(index):
            predecessor = predecessor.next

        new_node = ListNode(val, predecessor.next)
        predecessor.next = new_node

        self.size += 1



    def deleteAtIndex(self, index: int) -> None:
        
        if index < 0 or index >= self.size: 
            return 
        
        predecessor = self.dummy_node
        for _ in range(index):
            predecessor = predecessor.next
        
        predecessor.next = predecessor.next.next       
        self.size -= 1

        # ensuring the integrity of linked list and preventing 
        # potential issues or we can do below

        # delete_node = predecessor.next
        # predecessor.next = delete_node.next
        # delete_node.next = None



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)