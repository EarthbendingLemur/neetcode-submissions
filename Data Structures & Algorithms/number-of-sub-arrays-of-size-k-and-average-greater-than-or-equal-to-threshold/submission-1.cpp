class Solution {
public:
    int numOfSubarrays(vector<int>& arr, int k, int threshold) {

        int l = 0;
        int r = 0;
        int curSm = 0;
        int result = 0;

        while (r < arr.size())
        {

            while (r - l + 1 <= k)
            {
                curSm = curSm + arr[r];
                r++;
            }
            float avg = curSm / k;
            if (avg >= (float)threshold) result++;
            curSm = curSm - arr[l];
            l++;

        }


        return result;
        
    }
};