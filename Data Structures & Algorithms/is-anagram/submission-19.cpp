class Solution {
public:
    bool isAnagram(string s, string t) {
        std::unordered_map<char, int> s_map;

        for (int i = 0; i < s.size(); ++i)
        {
            if (!s_map.contains(s[i]))
            {
                s_map[s[i]] = 1;
            }
            else
            {
                s_map[s[i]]++;
            }
        }

        for (int i = 0; i < t.size(); ++i)
        {
            if (!s_map.contains(t[i]))
            {
                return false;
            }
            else
            {
                s_map[t[i]]--;
                if (s_map[t[i]] == 0)
                {
                    s_map.erase(t[i]);
                }
            }
        }


        return s_map.size() == 0;
    
    }
};
