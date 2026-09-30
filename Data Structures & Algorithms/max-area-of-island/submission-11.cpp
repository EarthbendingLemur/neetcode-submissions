#include <queue>
class Solution {
public:

    int islandSize(vector<vector<int>>& grid, vector<vector<bool>>& visited, int sr, int sc)
    {
        int res = 0;
        int rows = grid.size();
        int cols = grid[0].size();

        vector<pair<int, int>> dx = {
            {0, 1}, {0, -1}, {1, 0}, {-1, 0}
        };

        queue<pair<int, int>> q;
        q.push({sr, sc});
        visited[sr][sc] = true;

        while (q.size() > 0)
        {
            auto [r, c] = q.front();
            res++;
            q.pop();

            for (auto [dr, dc] : dx)
            {
                int nr = dr + r;
                int nc = dc + c;

                if (nr < 0 || nr == rows || nc < 0 || nc == cols) continue;
                if (grid[nr][nc] != 1 || visited[nr][nc]) continue;

                q.push({nr, nc});
                visited[nr][nc] = true;
            }
        }

        return res;
    }
    int maxAreaOfIsland(vector<vector<int>>& grid) {

        vector<vector<bool>> visited(grid.size(), vector<bool>(grid[0].size(), false));
        int result = 0;
        for (int r = 0; r < grid.size(); ++r)
        {
            for (int c = 0; c < grid[0].size(); ++c)
            {
                if (grid[r][c] == 1 && !visited[r][c])
                {
                    result = max(result, islandSize(grid, visited, r, c));
                }
            }
        }

        return result;
    }
};
