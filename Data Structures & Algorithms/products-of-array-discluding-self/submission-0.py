class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [None] * len(nums)
        post = [None] * len(nums)
        sol = [None] * len(nums)

        for i,n in enumerate(nums):
            if i == 0: 
                pre[i] = n
            else:
                pre[i] = n * pre[i - 1]

        
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                post[i] = nums[i]
            else:
                post[i] = nums[i] * post[i + 1]

        
        for i in range(len(sol)):
            prefix = 1
            postfix = 1
            if i > 0:
                prefix = pre[i - 1]
            if i < len(sol) - 1:
                postfix = post[i + 1]
            sol[i] = prefix * postfix

        print(pre)
        print(post)
        return sol
        