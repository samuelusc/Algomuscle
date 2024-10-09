class MyLinkedList:

    def __init__(self):
        self.dummy = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return
        cur = self.dummy.next
        for i in range(index):
            cur = cur.next

        return cur.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        pre = self.dummy
        for i in range(index):
            pre = pre.next
        node = ListNode(val)
        node.next = pre.next
        pre.next = node
        self.size += 1



    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        
        pre = self.dummy
        for i in range(index):
            pre = pre.next
        
        pre.next = pre.next.next
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)