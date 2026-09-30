#include <unordered_map>
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {

        unordered_map<int, int> mp;
        mp[0] = 1;
        
        int prefix = 0;
        int res = 0;

        for (const auto& num : nums)
        {
            prefix = prefix + num;

            if (mp.contains(prefix - k))
            {
                res = res + mp[prefix - k];
            }
            mp[prefix]++;
        }

        return res;
        
    }
};