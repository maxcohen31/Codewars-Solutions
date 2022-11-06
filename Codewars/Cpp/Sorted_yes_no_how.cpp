#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

std::string is_sorted_and_how(std::vector<int> array)
{
    if(std::is_sorted(std::begin(array), std::end(array)))
    {
        return "yes, ascending";
    }
    else if(std::is_sorted(std::begin(array), std::end(array), std::greater<int>()))
    {
        return "yes, descending";
    }
    else
    {
        return "no";
    }
    
}


int main(){

    std::vector<int> vec {1, 2, 3};
    std::vector<int> vec2 {15, 7, 3, -8};
    std::string result = is_sorted_and_how(vec);
    std::string result2 = is_sorted_and_how(vec2);
    std::cout << result;
    std::cout << result2;

    return 0;
}