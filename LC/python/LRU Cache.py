class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        LRUCache.capacity = capacity
        LRUCache.stack = []
        LRUCache.dict = {}

    # @return an integer
    def get(self, key):
        if key in LRUCache.dict:
            LRUCache.stack.remove(key)
            LRUCache.stack.append(key)
            return LRUCache.dict[key]
        else:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in LRUCache.stack:
            LRUCache.stack.remove(key)
            LRUCache.stack.append(key)
        else:
            if len(LRUCache.stack)+1<=LRUCache.capacity:
                LRUCache.stack.append(key)
            else:
                old = LRUCache.stack.pop(0)
                del LRUCache.dict[old]
                LRUCache.stack.append(key)
        LRUCache.dict[key] = value
                
