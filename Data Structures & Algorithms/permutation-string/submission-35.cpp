#include <iostream>
#include <unordered_map>
using std::cout, std::endl;

class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        unordered_map<char, int> s1_mp;
        for (const auto& c : s1) s1_mp[c]++;
        bool found = false;
        for (size_t l = 0; l < s2.size(); ++l)
        {
            if (!s1_mp.contains(s2[l])) continue;

            size_t r = l;
            unordered_map<char, int> window = s1_mp;
            while (r < s2.size() && (r - l + 1) <= s1.size())
            {
                if (!window.contains(s2[r])) break;

                window[s2[r]]--;
                if (window[s2[r]] == 0) window.erase(s2[r]);
                r++;
            }
            if (window.size() == 0) found = true;
        }

        return found;
        
    }
};
