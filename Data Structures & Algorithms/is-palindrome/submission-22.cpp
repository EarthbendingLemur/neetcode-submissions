class Solution {
public:
#include <regex>
    bool isPalindrome(string s) {
        
        char* left = s.data();
        char* right = s.data() + s.size() - 1;


        while (left < right)
        {   
            while (left < right && !std::isalnum(*left))
            {
                left++;
            }
            while (left < right && !std::isalnum(*right))
            {
                right--;
            }

            if (std::tolower(*left) != std::tolower(*right)) return false;

            left++;
            right--;
        }
        return true;
    }
};
