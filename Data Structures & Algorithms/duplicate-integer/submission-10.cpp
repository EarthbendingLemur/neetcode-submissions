class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> numsSet;

        for (int i = 0; i < nums.size(); ++i)
        {
            numsSet.insert(nums.at(i));
        }

        if (numsSet.size() == nums.size())
        {
            return false;
        }
        else 
        {
            return true;
        }
    }
};