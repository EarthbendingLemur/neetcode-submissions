class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {

        int left = 0;
        int right = numbers.size() - 1;

        while (left < right)
        {
            int sm = numbers[left] + numbers[right];
            if (sm == target)
                return {left + 1, right + 1};
            else if (sm < target)
                left++;
            else
                right--;
        }

        return {-1, -1};
        
    }
};
