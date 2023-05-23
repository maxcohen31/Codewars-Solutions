#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

std::vector<int> solve(const std::vector<std::string> &a, const std::vector<std::string> &b)
{
    int count;
    std::vector<int> result;
    
    for(auto b_value : b)
    {
        count = 0;
        for(auto a_value : a)
        {
            if(b_value == a_value)
            {
                count++;
            }
        }
        result.push_back(count);
    }
    return result;

}

// Alternative Solution
std::vector<int> solve2(const std::vector<std::string> &a, const std::vector<std::string> &b)
{
    std::vector<int> result;
    for(auto &i : b)
    {
        result.push_back(std::count(a.begin(), a.end(), i));
    }
    return result;
}

int main(){

    std::vector<std::string> arr1 {"abc", "abc", "xyz", "cde", "uvw"};
    std::vector<std::string> arr2 {"abc", "cde", "uap"};

    std::vector<int> r = solve(arr1, arr2);
    
    for(const int i : r) { std::cout << i << "\n"; }

    return 0;
}