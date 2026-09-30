#include <vector>
#include <unordered_set>
#include <queue>

class Solution {
public:

    vector<string> findNeighbours(const string& word, unordered_set<string>& wordListSet)
    {
        vector<string> res;
        
        for (int i = 0; i < word.size(); ++i)
        {
            string copy = word;
            for (int c_iter = 0; c_iter < 26; ++c_iter)
            {
                copy[i] = static_cast<char>(c_iter + 'a');
                if (wordListSet.contains(copy))
                    res.push_back(copy);
            }
        }

        return res;
    }  

    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        queue<pair<string, int>> q;
        unordered_set<string> visited;
        unordered_set<string> wordListSet;
        for (const auto& word : wordList)
        {
            wordListSet.insert(word);
        }
        visited.insert(beginWord);
        q.push({beginWord, 0});
        
        while (!q.empty())
        {
            auto [word, steps] = q.front();
            q.pop();
            if (word == endWord)
                return steps + 1;

            for (const auto& neigh : findNeighbours(word, wordListSet))
            {   
                if (visited.contains(neigh))
                    continue;
                
                q.push({neigh, steps + 1});
                visited.insert(neigh);            
            }
        }

        return 0;
    }
};
