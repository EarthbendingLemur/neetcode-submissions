#include <unordered_map>

class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        unordered_map<int, int> counts;

        int l = 0;
        int res = 0;
        for (int r = 0; r < fruits.size(); ++r)
        {
            counts[fruits[r]]++;

            while (counts.size() > 2)
            {
                counts[fruits[l]]--;
                if (counts[fruits[l]] == 0)
                    counts.erase(fruits[l]);
                l++;
            }
            int tmpsum = 0;
            for (const auto& [key, freq] : counts)
            {
                tmpsum += freq;
            }

            res = max(res, tmpsum);
                        
        }

        return res;

    }
};