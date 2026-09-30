#include <unordered_map>
class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, int> hmp;

        for (int i = 0; i < nums.size(); ++i) {
            if (hmp.find(nums.at(i)) != hmp.end()) {
                return true;
            }
            else {
                hmp.insert({nums.at(i),0});
            }
        }
        return false;

    }
};
