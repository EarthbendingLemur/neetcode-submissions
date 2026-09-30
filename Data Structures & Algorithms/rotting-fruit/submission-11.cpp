#include <queue>

class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {

        int ROWS = grid.size();
        int COLS = grid[0].size();
        queue<pair<int, int>> q;

        int dx[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        int fresh = 0;
        for (int r = 0; r < ROWS; ++r)
        {
            for (int c = 0; c < COLS; ++c)
            {
                if (grid[r][c] == 2)
                    q.push({r, c});
                else if (grid[r][c] == 1)
                    fresh++;
            }
        }
        if (fresh == 0) return 0;
        int timesteps = 0;

        while (!q.empty() and fresh > 0)
        {
            int q_size = q.size();
            for (int it = 0 ; it < q_size; ++ it)
            {
                auto [r, c] = q.front();
                q.pop();

                for (const auto& [dr, dc] : dx)
                {
                    int nr = dr + r;
                    int nc = dc + c;

                    if (nr < 0 || nr == ROWS || nc < 0 || nc == COLS) continue;
                    if (grid[nr][nc] != 1) continue;
                    grid[nr][nc] = 2;
                    q.push({nr, nc});
                    fresh--;
                }
            }
            timesteps++;
        }


        return fresh == 0 ? timesteps : -1;
        
    }
};
