#include <queue>
class Solution {
public:
    void BFS(vector<pair<int, int>>& sources, vector<vector<int>>& heights, vector<vector<bool>>& visited)
    {
        int ROWS = visited.size();
        int COLS = visited[0].size();
        vector<pair<int, int>> dx = {
            {0, 1}, {0, -1}, 
            {1, 0}, {-1, 0}
        };

        queue<pair<int, int>> q;
        for (auto [r, c] : sources)
        {
            q.push({r, c});
            visited[r][c] = true;
        }

        while (!q.empty())
        {
            auto [r, c] = q.front();
            q.pop();

            for (auto [dr, dc] : dx)
            {
                int nr = dr + r;
                int nc = dc + c;

                if (nr < 0 || nr == ROWS || nc < 0 || nc == COLS) continue;
                if (visited[nr][nc] || heights[nr][nc] < heights[r][c]) continue;
                q.push({nr, nc});
                visited[nr][nc] = true;
            }

        }

    }


    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        int ROWS = heights.size();
        int COLS = heights[0].size();

        vector<vector<bool>> pac_visited(ROWS, vector<bool>(COLS, false));
        vector<vector<bool>> atl_visited(ROWS, vector<bool>(COLS, false));
        vector<pair<int, int>> pac_sources;
        vector<pair<int, int>> atl_sources;

        for (int c = 0; c < COLS; ++c)
        {
            pac_sources.push_back({0, c});
            atl_sources.push_back({ROWS - 1, c});
        }   

        for (int r = 0; r < ROWS; ++r)
        {
            pac_sources.push_back({r, 0});
            atl_sources.push_back({r, COLS - 1});
        }    

        BFS(pac_sources, heights, pac_visited);
        BFS(atl_sources, heights, atl_visited);


        vector<vector<int>> result;
        for (int r = 0; r < ROWS; ++r)
        {
            for (int c = 0; c < COLS; ++c)
            {
                if (pac_visited[r][c] && atl_visited[r][c]) result.push_back({r, c});
            }
        }

        return result;
    }
};
