#include <queue>

class Solution {
public:

    void BFS(int sr, int sc, vector<vector<bool>>& visited, vector<vector<char>>& grid)
    {
        int ROWS = grid.size();
        int COLS = grid[0].size();
        vector<pair<int, int>> dx = {
            {0, 1}, {0, -1}, 
            {1, 0}, {-1, 0}
        };

        queue<pair<int, int>> q;
        q.push({sr, sc});
        visited[sr][sc] = true;
        while (!q.empty())
        {
            auto [r, c] = q.front();
            q.pop();

            for (const auto&[dr, dc] : dx)
            {
                int nr = dr + r;
                int nc = dc + c;
                if (nr < 0 || nr == ROWS || nc < 0 || nc == COLS || 
                    visited[nr][nc] || grid[nr][nc] != '1') continue;
                
                q.push({nr, nc});
                visited[nr][nc] = true;
            }
        }

    }

    int numIslands(vector<vector<char>>& grid) {
        int ROWS = grid.size();
        int COLS = grid[0].size();

        vector<vector<bool>> visited(ROWS, vector<bool>(COLS, false));
        int numIslands = 0;

        for (int r = 0; r < ROWS; ++r)
        {
            for (int c = 0; c < COLS; ++c)
            {
                if (grid[r][c] == '1' && !visited[r][c])
                {
                    BFS(r, c, visited, grid);
                    numIslands += 1;
                } 
            }
        }
        
        return numIslands;
    }
};
