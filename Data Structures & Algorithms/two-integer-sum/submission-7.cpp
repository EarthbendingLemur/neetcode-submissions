class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> complements;
        int index = 0;
        for (const auto& num: nums)
        {
            if (complements.contains(num))
            {
                return {complements[num], index};
            }

            complements[target - num] = index;
            ++index;
        }

        return {-1, -1};
    }
};
