class Node:
    def __init__(self,key,val):
        self.key,self.val = key,val
        self.pre = self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left,self.right = Node(0,0),Node(0,0)
        self.left.next, self.right.pre = self.right,self.left

    def remove(self,node):
        prev,nxt = node.pre, node.next
        prev.next,nxt.pre = nxt, prev

    def insert(self,node):
        prev,nxt = self.right.pre, self.right
        prev.next = nxt.pre = node
        node.pre, node.next = prev, nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)