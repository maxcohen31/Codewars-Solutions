#include <vector>
#include <iostream>
#include <set>

bool contains_all(const std::vector<int>& arr, const std::vector<int>& target) {
    
    std::set<int> result;

    for(int i=0; i<arr.size(); i++)
    {
        result.emplace(arr[i]);
    }

    int size_result = result.size();

    for(int i=0; i<target.size(); i++)
    {
        result.emplace(target[i]);
    }

    if(result.size() == size_result)
    {
        return true;
    }
    else
    {
        return false;
    }
}

int main(){

    std::vector<int> v1 {1, 2, 3, 4, 5};
    std::vector<int> v2 {1, 2, 3};
    bool result = contains_all(v1, v2);
    std::cout << result;

    return 0;
}