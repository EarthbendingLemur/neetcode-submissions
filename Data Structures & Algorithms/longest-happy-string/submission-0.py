class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:


        res = ""
        heap = []
        if a > 0:
            heapq.heappush(heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(heap, (-c, 'c'))
        

        while heap:
            count, char = heapq.heappop(heap)
            if len(res) >= 2 and res[-1] == char and res[-2] == char:
                if not heap:
                    break

                count2, char2 = heapq.heappop(heap)
                res += char2
                count2 += 1
                if count2 < 0:
                    heapq.heappush(heap, (count2, char2))
                
                heapq.heappush(heap, (count, char))
            else:
                res += char
                count += 1
                if count < 0:
                    heapq.heappush(heap, (count, char))
        return res