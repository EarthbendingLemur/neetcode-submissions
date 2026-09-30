class Solution:
    def isPathCrossing(self, path: str) -> bool:
        dx = {
            'N':(0, 1),
            'S':(0, -1),
            'W':(-1, 0),
            'E':(1, 0)
        }

        pos = [0, 0]
        trace = set()
        trace.add(tuple(pos))
        for c in path:
            pos[0] += dx[c][0]
            pos[1] += dx[c][1]
            if tuple(pos) in trace:
                return True
            trace.add(tuple(pos))
        
        return False