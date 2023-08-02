#include <algorithm>
#include <iostream>
#include <vector>


template <typename T>
std::vector<T> find_array(std::vector<T> arr1, std::vector<int> arr2)
{   
    std::vector<T> result;
    if(arr1.size() == 0 || arr2.size() == 0)
    {
        return result;
    }
    for(auto element : arr2)
        if(element <= arr1.size())
        {
            result.push_back(arr1[element]);
        }
    return result;
    
}



int main(){



    return 0;
}
