#include <queue>

class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();

        vector<pair<int, int>> dx = { 
            { 0,  1}, 
            { 0, -1}, 
            { 1,  0}, 
            {-1,  0}
            };
        queue<pair<int, int>> q;
        int num_fresh = 0;
        for (int r = 0; r < rows; ++r)
        {
            for (int c = 0; c < cols; ++c)
            {
                if (grid[r][c] == 2)
                {
                    q.push({r, c});
                }
                else if (grid[r][c] == 1)
                {
                    num_fresh++;
                }
            }
        }

        int time = 0;
        while (!q.empty() and num_fresh > 0)
        {
            int len_q = q.size();
            for (int i = 0; i < len_q; ++i)
            {
                auto [r, c] = q.front();
                q.pop();

                for (const auto& [dr, dc] : dx)
                {
                    int nr = dr + r;
                    int nc = dc + c;
                    if (nr < 0 || nr == rows || 
                        nc < 0 || nc == cols || 
                        grid[nr][nc] != 1) continue;

                    grid[nr][nc] = 2;
                    num_fresh--;
                    q.push({nr, nc});
                }

            }
            time++;
        }

        if (num_fresh == 0) return time;
        return -1;
    }
};
