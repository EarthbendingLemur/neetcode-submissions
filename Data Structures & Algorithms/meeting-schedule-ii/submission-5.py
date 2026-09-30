"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x:x.start)

        meetings_heap = []

        for interval in intervals:
            m_start = interval.start
            m_end = interval.end

            if not meetings_heap:
                heapq.heappush(meetings_heap, (m_end, m_start))
                continue
            
            if meetings_heap[0][0] > m_start:
                heapq.heappush(meetings_heap, (m_end, m_start))
            else:
                heapq.heappop(meetings_heap)
                heapq.heappush(meetings_heap, (m_end, m_start))
                
        print(meetings_heap)
        return len(meetings_heap)
