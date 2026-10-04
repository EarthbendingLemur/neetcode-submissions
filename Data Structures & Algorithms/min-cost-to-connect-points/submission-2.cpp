#include <queue>
#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>

struct PairHash 
{
    size_t operator()(const pair<int, int>& p) const 
    {
        return hash<int>{}(p.first) ^ (hash<int>{}(p.second) << 1);
    }
};

class Solution {
public:
    int minCostConnectPoints(vector<vector<int>>& points) {

        
        unordered_map<pair<int, int>, vector<vector<int>>, PairHash> adj;
        unordered_set<pair<int, int>, PairHash> visited;
        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> mh;

        
        for (int i = 0; i  < points.size(); ++i)
        {
            for (int j = i + 1; j < points.size(); ++j)
            {
                int dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]);
                adj[{points[i][0], points[i][1]}].push_back({dist, points[j][0], points[j][1]});
                adj[{points[j][0], points[j][1]}].push_back({dist, points[i][0], points[i][1]});
            }
        }

        mh.push({0, points[0][0], points[0][1]});
        int result = 0;

        while (!mh.empty())
        {
            auto node = mh.top();
            mh.pop();
            if (visited.contains({node[1], node[2]})) continue;
            visited.insert({node[1], node[2]});
            result  = result + node[0];
            
            if (visited.size() == points.size()) return result;

            for (const auto& neighb: adj[{node[1], node[2]}])
            {
                mh.push({neighb[0], neighb[1] , neighb[2]});
            }
        }

        return -1;
    }
};
