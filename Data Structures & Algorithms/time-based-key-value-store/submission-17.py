class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)
                

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        
        arr = self.timeMap[key]
        if not arr:
            return ""
        
        L, R = 0, len(arr) - 1
        res = -1
        while L <= R:
            M = (L + R) // 2
            if arr[M][0] <= timestamp:
                res = M
                L = M + 1
            else:
                R = M - 1
        return "" if res == -1 else arr[res][1]        
