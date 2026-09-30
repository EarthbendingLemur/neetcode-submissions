#include <queue>
#include <unordered_set>
class Solution {
public:


    void solve(vector<vector<char>>& board) {
        int ROWS = board.size();
        int COLS = board[0].size();

        int dx[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        queue<pair<int, int>> q;
        for (int c = 0; c < COLS; ++c)
        {
            if (board[0][c] == 'O')
            {
                q.push({0, c});
                board[0][c] = '+';
            }
            if (board[ROWS - 1][c] == 'O')
            {
                q.push({ROWS - 1, c});
                board[ROWS - 1][c] = '+';
            }
                
        }

        for (int r = 0; r < ROWS; ++r)
        {
            if (board[r][0] == 'O')
            {
                q.push({r, 0});
                board[r][0] = '+';
            }               
            if (board[r][COLS - 1] == 'O')
            {
                q.push({r, COLS - 1});
                board[r][COLS - 1] = '+';
            }  
        }


        // DO BFS from every node in queue
        while (!q.empty())
        {
            auto [r, c] = q.front();
            q.pop();

            for (const auto& [dr, dc] : dx)
            {
                int nr = dr + r;
                int nc = dc + c;

                if (nr < 0 || nr == ROWS || nc < 0 || nc == COLS) continue;
                if (board[nr][nc] != 'O') continue;

                q.push({nr, nc});
                board[nr][nc] = '+';
            }
        }

        for (int r = 0; r < ROWS; ++r)
        {
            for (int c = 0; c < COLS; ++c)
            {
                // unmark board and surround islands
                if (board[r][c] == '+')
                    board[r][c] = 'O';
                else if (board[r][c] == 'O')
                    board[r][c] = 'X';
            }
        }
    }   
};
