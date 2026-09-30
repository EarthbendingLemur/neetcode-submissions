class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:

        mapping = defaultdict(list)
        for i in range(len(username)):
            mapping[username[i]].append((website[i], timestamp[i]))
        
        for _, hist in mapping.items():
            hist.sort(key=lambda x:x[1])

        patterns = defaultdict(set)

        for u, hist in mapping.items():

            for i in range(len(hist)):
                for j in range(i + 1, len(hist)):
                    for k in range(j + 1, len(hist)):
                        pattern = (hist[i][0], hist[j][0], hist[k][0])
                        patterns[pattern].add(u)
        
        best = None
        best_count = 0

        
        for pattern, users in patterns.items():
            if len(users) > best_count:
                best_count = len(users)
                best = pattern
                continue
            
            if len(users) == best_count:
                if pattern < best:
                    best = pattern
            

        return list(best)
