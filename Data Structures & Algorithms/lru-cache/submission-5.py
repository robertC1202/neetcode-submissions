class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):

        #set capacity equal to capacity
        #Initialize hashMap / cache
        #initialize two dummy nodes that will help us maintin LRU vs MRU 
        self.cap = capacity
        self.cache = {}

        self.right = ListNode(0,0)
        self.left = ListNode(0,0)

        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])

            return self.cache[key].value
        
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = ListNode(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:

            #remove the left most node from the list
            lru = self.left.next
            self.remove(lru)

            del self.cache[lru.key]
    
    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev
    
    def insert(self, node):
        prev = self.right.prev
        right = self.right

        node.next = right
        node.prev = prev

        prev.next = node
        right.prev = node
    
        
       
        
   
        
        
