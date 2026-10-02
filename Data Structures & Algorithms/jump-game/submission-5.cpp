class Solution {
public:
    bool canJump(vector<int>& nums) {

        int jumpReq = 1;

        for (int i = nums.size() - 2; i >= 0; --i)
        {
            if (nums[i] >= jumpReq)
            {
                jumpReq = 1;
            }
            else
            {
                jumpReq++;
            }
        }

        return (jumpReq == 1) ? true : false;        
    }
};
