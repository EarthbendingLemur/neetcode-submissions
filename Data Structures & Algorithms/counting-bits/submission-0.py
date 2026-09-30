class Solution:
    def countBits(self, n: int) -> List[int]:
        cnt = [0]
        for i in range(1, n + 1):
            cnt.append(cnt[i >> 1] + i % 2)
        return cnt
