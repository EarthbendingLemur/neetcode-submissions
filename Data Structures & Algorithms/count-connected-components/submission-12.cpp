#include <unordered_map>
#include <queue>
class Solution {
public:

    int countComponents(int n, vector<vector<int>>& edges) {

        unordered_map<int, vector<int>> adj;

        for (const auto& edge : edges)
        {
            int a = edge[0];
            int b = edge[1];
            adj[a].push_back(b);
            adj[b].push_back(a);
        }
        int res = 0;
        vector<bool> visited(n, false);
        for (int i = 0; i < n; ++i)
        {
            if (visited[i])
                continue;
            
            queue<int> q;
            q.push(i);
            visited[i] = true;
            res++;
            while (!q.empty())
            {
                int node = q.front();
                q.pop();

                for (const auto& neigh : adj[node])
                {
                    if (visited[neigh]) 
                        continue;

                    q.push(neigh);
                    visited[neigh] = true;
                }
            }
        }


        return res;
    }
};
