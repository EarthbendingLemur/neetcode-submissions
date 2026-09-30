#include <queue>
#include <unordered_set>

class Solution {
public:
    struct PairHash {
        size_t operator()(const std::pair<int, int>& p) const 
        {
            return (hash<int>{}(p.first)) ^ (hash<int>{}(p.second) << 1);
        }
    };

    int islandPerimeter(vector<vector<int>>& grid) {
        size_t result = 0;
        queue<std::pair<int, int>> q;
        unordered_set<std::pair<int, int>, PairHash> visited;


        size_t rows = grid.size();
        size_t cols = grid[0].size();
        vector<std::pair<int, int>> dx = { {0, 1}, {0, -1}, {1, 0}, {-1, 0} };


        for (size_t r = 0; r < rows; ++r)
        {
            for (size_t c = 0; c < cols; ++c)
            {
                if (grid[r][c] == 1)
                {
                    q.push({r, c});
                    visited.insert({r, c});
                    break;
                }
            }
        }

        while (!q.empty())
        {
            auto& [r, c] = q.front();
            q.pop();
            int numNeighbours = 0;
            for (const auto& [dr, dc] : dx)
            {
                int nr = dr + r;
                int nc = dc + c;
                if (nr < 0 || nr == rows || nc < 0 || nc == cols || grid[nr][nc] == 0) continue;
                numNeighbours++;
                if (visited.contains({nr, nc})) continue;
                q.push({nr, nc});
                visited.insert({nr, nc});
            }
            result = result + 4 - numNeighbours;
        }        

        return result;
    }
};