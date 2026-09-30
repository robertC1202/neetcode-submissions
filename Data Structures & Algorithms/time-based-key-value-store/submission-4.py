class TimeMap:

    def __init__(self):
        self.hashMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashMap:
            self.hashMap[key] = []
        
        self.hashMap[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashMap: 
            return ''
        
        lst = self.hashMap[key]

        if timestamp < lst[0][0]:
            return ''
        
        n = len(lst)
        l = 0
        r = n - 1

        while l < r: 
            mid = (l+r+1) // 2

            mid_timestamp = lst[mid][0]

            if mid_timestamp > timestamp:
                r = mid - 1
            elif mid_timestamp < timestamp:
                l = mid
            else:
                return lst[mid][1]
        
        return lst[l][1]
        



