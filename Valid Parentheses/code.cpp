#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;

class Solution
{
public:
    bool isValid(string s)
    {
        vector<char> stack;
        map<char, char> pairs = {{'(', ')'}, {'[', ']'}, {'{', '}'}};
        for (const auto &bracket : s)
        {
            if (pairs.find(bracket) != pairs.end())
                stack.push_back(bracket);
            else
            {
                if(stack.empty())
                    return false;
                if(bracket != pairs[stack.back()])
                    return false;
                stack.pop_back();
            }
        }
        return stack.empty();
    }
};