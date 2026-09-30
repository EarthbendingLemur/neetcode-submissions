class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = {}

        for i,n in enumerate(nums):
            mp[n] = i
        max_l = 0
        for i, n in enumerate(nums):

            if (n - 1) not in mp:
                l = 0
                seq_n =  n 
                while seq_n in mp:
                    print(seq_n)
                    seq_n += 1
                    l += 1
                
                max_l = max(max_l, l)
        
        return max_l
            