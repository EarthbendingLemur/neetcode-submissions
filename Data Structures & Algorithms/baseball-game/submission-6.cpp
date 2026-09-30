#include <stack>
#include <iostream>
#include <string>
class Solution {
public:
    int calPoints(vector<string>& operations) {

        stack<int> stk;

        for (const auto& op : operations)
        {
            if (op == "+")
            {
                int v1 = stk.top();
                stk.pop();
                int v2 = stk.top();
                stk.push(v1);
                stk.push(v1 + v2);
            }
            else if (op == "C")
            {
                stk.pop();
            }
            else if (op == "D")
            {
                stk.push(stk.top() * 2);
            }
            else 
            {
                stk.push(std::stoi(op));
            }
        }



        int result = 0;
        while (!stk.empty())
        {
            result = result + stk.top();
            stk.pop();
        }
        return result;
    }
};