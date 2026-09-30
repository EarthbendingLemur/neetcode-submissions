class Solution:
    def reorganizeString(self, s: str) -> str:
        hp = []
        mp = defaultdict(int)
        for c in s:
            mp[c] += 1
        
        for c, freq in mp.items():
            heapq.heappush(hp, (-freq, c))

        res = []
        while hp:
            cur_freq, c = heapq.heappop(hp)
            if not res or res[-1] != c:
                res.append(c)
                cur_freq += 1
                if cur_freq:
                    heapq.heappush(hp, (cur_freq, c))
            else:
                if not hp:
                    return ""
                
                second_freq, second_c = heapq.heappop(hp)
                res.append(second_c)
                second_freq += 1
                if second_freq:
                    heapq.heappush(hp, (second_freq, second_c))

                heapq.heappush(hp, (cur_freq, c))
        
        print(res)
        return ('').join(res) if len(res) == len(s) else ""
