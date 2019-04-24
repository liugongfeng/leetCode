class LinkedList:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None



class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = dict()
        self.head = LinkedList(0, 0)
        self.tail = LinkedList(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        if key in self.d:
            node = self.d.get(key)
            self._remove(node)
            self._add(node)
            return node.val
        return -1   # key does not exists (Not Found)


    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self._remove(self.d.get(key))
        node = LinkedList(key, value)
        self._add(node)
        self.d[key] = node
        if len(self.d) > self.capacity:
            delete_node = self.head.next
            self.d.pop(delete_node.key)
            self._remove(delete_node)


    """ Private method
    Before: prevNode <-> node <-> nextNode
    After:  prevNode <-> nextNode
    """
    def _remove(self, node: LinkedList) -> None:
        p = node.prev
        n = node.next
        n.prev = p
        p.next = n


    """     Private method
    Before: prev_node <-> tail;
    After:  prev_node <-> newNode <-> tail;
    """
    def _add(self, node: LinkedList) -> None:
        p = self.tail.prev
        p.next = node
        node.next = self.tail
        node.prev = p
        self.tail.prev = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)