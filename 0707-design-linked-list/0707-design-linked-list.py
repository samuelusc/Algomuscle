class MyLinkedList:
    #design scratch 
    def __init__(self):
        # Create a dummy node
        self.dummy_node = ListNode()
        # Initialize node counter and length
        self.size = 0

    def get(self, index: int) -> int:
        # Boundary check
        if index < 0 or index >= self.size:
            return  -1

        # Start from the head, there will be at least one node
        current_node = self.dummy_node.next

        # Iterate to the next node based on index
        for _ in range(index):
            current_node = current_node.next
        
        return current_node.val

    def addAtHead(self, val: int) -> None:
        # Invoke addAtIndex and assign (0, val)
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        # Invoke addAtIndex and assign (self.size, val)
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        # Check for index out of bounds
        if index < 0 or index > self.size:
            return
        
        # Assign the dummy node to predecessor
        predecessor = self.dummy_node

        # Find the predecessor of the node to be added
        for _ in range(index):
            predecessor = predecessor.next
        
        # Create the new node and maintain the predecessor's link
        add_node = ListNode(val, predecessor.next)
        # Link the predecessor with the new node
        predecessor.next = add_node

        # Don't forget to increment self.size by 1 for each added node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        # Check boundaries
        if index < 0 or index >= self.size:
            return 
        
        # Like in addAtIndex, first find the predecessor
        predecessor = self.dummy_node
        for _ in range(index):
            predecessor = predecessor.next
        
        # The predecessor skips the node to be deleted
        predecessor.next = predecessor.next.next
        # Don't forget to decrement self.size by 1
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)