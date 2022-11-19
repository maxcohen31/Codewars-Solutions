#include <vector>
#include <iostream>
#include <algorithm>

int min(std::vector<int> list){
    
    int min_int = list[0];
    for(size_t i{0}; i < list.size(); ++i)
    {
        if(list[i] < min_int){
            min_int = list[i];
        }
    }
    return min_int;
}

int max(std::vector<int> list){
    
    int max_int = list[0];
    for(size_t i{0}; i < list.size(); ++i)
    {
        if(list[i] > max_int)
        {
            max_int = list[i];
        }
    }
    return max_int;
}

// Alternative Solution
int min(const std::vector<int>& list) {
    return *std::min_element(list.begin(), list.end());
}

int max(const std::vector<int>& list) {
    return *std::max_element(list.begin(), list.end());
}
