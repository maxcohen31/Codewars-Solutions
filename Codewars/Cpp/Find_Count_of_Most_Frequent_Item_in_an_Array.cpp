#include <iostream>
#include <map>
#include <vector>

unsigned int most_frequent_item_count(const std::vector<int>& collection) {;
    std::map<int, int> map_vector;
    int counter {0};
    for(int i = 0; i < collection.size(); ++i)
    {
        map_vector[collection[i]]++;
    }
    for(auto i : map_vector)
    {
        // std::cout << "[ " << i.first << ": " << i.second << " ]";
        if(counter < i.second)
        {
            counter = i.second;
        }
    
    }

    return counter;
}

int main(){
    std::vector<int> v {1, 2, 2, 3, 5};
    std::cout << most_frequent_item_count(v);


    return 0;
}