class Solution {
public:
    int appendCharacters(string s, string t) {
        int t_ptr = 0;
        for(int s_ptr = 0; s_ptr < s.size(); ++s_ptr)
        {
            if (s[s_ptr] == t[t_ptr])
            {
                t_ptr++;
                if (t_ptr == t.size()) return 0;
            }
        }

        return t.size() - t_ptr;
        
    }
};