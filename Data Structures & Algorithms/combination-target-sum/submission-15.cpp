        // res = []

        // def backtrack(idx, sm, sol):
        //     if sm == target:
        //         res.append(sol[:])
        //         return
            
        //     if idx >= len(nums) or sm > target:
        //         return
            
        //     sol.append(nums[idx])
        //     backtrack(idx, sm + nums[idx], sol)
        //     sol.pop()
        //     backtrack(idx + 1, sm, sol)
        
        // backtrack(0, 0, [])
        // return res
            



class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        vector<vector<int>> res;
        vector<int> sol;
        backtrack(res, nums, target, 0, 0, sol);
        return res;
    }

    void backtrack(vector<vector<int>>& res, vector<int>& nums, int target, int idx, int sm, vector<int>& sol)
    {
        if (sm == target)
        {
            vector<int> copy_sol = sol;
            res.push_back(copy_sol);
            return;
        }

        if (idx >= nums.size() || sm > target) return;

        sol.push_back(nums[idx]);
        backtrack(res, nums, target, idx, sm + nums[idx], sol);
        sol.pop_back();
        backtrack(res, nums, target, idx + 1, sm, sol);
    }
};
