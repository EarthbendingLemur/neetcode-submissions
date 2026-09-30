#include <iostream>
#include <unordered_set>
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {

        unordered_set<int> window;

        int l = 0;
        int r = 0;

        while (r < nums.size())
        {
            if (r - l <= k)
            {
                if (window.contains(nums[r])) return true;
                window.insert(nums[r]);
                r++;
            }
            else
            {
                window.erase(nums[l]);
                l++;
            }
        }

        return false;
    }
};