#include <queue>
class Solution {
public:

    int BFS(const int& sr,const int& sc, vector<vector<int>>& grid)
    {
        vector<pair<int, int>> dx = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        int rows = grid.size();
        int cols = grid[0].size();
        queue<pair<int, int>> q;
        q.push({sr, sc});
        grid[sr][sc] = -1;
        int sze = 0;

        while  (!q.empty())
        {
            auto [r, c] = q.front();
            q.pop();

            sze++;  
            for (const auto& [dr, dc] : dx)
            {
                int nr = dr + r;
                int nc = dc + c;
                if (nr < 0 || nr == rows || nc < 0 || nc == cols) continue;
                if (grid[nr][nc] != 1) continue;
                q.push({nr, nc});
                grid[nr][nc] = -1;
            }
        }

        return sze;
    }
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        
        int rows = grid.size();
        int cols = grid[0].size();
        int res = 0;
        for (int r = 0; r < rows; ++r)
        {
            for (int c = 0; c < cols; ++c)
            {
                if (grid[r][c] == 1)
                {
                    res = max(BFS(r, c, grid), res);
                }
            }
        }
        
        return res;
    }
};
