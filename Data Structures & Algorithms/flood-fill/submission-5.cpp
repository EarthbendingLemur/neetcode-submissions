class Solution {
#include <queue>
#include <unordered_set>

public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        int ROWS = image.size();
        int COLS = image.at(0).size();
        std::vector<pair<int, int>> dx = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        queue<pair<int, int>> q;
        q.push({sr, sc});
        int sourceColour = image.at(sr).at(sc);
        std::vector<std::vector<bool>> visited(ROWS, std::vector<bool>(COLS, false));
        visited[sr][sc] = true;

        while (q.size() > 0)
        {
            auto [row, col] = q.front();
            q.pop();
            image.at(row).at(col) = color;

            for (auto [dr, dc] : dx)
            {
                int nr = dr + row;
                int nc = dc + col;
                if (nr < 0 || nr == ROWS || nc < 0 || nc == COLS or image.at(nr).at(nc) != sourceColour) continue;
                if (visited[nr][nc]) continue;

                q.push({nr, nc});
                visited[nr][nc] = true;
            }
        }


        return image;
    }
};