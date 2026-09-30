class Solution {
public:
    vector<int> findBuildings(vector<int>& heights) {

        vector<int> result;
        result.push_back(heights.size() - 1);
        int maxHeight = heights[heights.size() - 1];
        for (int i = heights.size() - 2; i >= 0; --i)
        {
            if (heights[i] > maxHeight) 
            {
                result.push_back(i);
                maxHeight = heights[i];
            }
        }
        reverse(result.begin(), result.end());
        return result;
    }
};