#include <algorithm>
#include <string>
#include <iostream>
#include <vector>
#include <sstream>

std::string highAndLow(const std::string& numbers){
    std::vector<int> numbs;
    std::string result;
    std::istringstream iss(numbers);
    int num; 

    while(iss >> num)
    {
        numbs.push_back(num);
    }

    std::sort(numbs.begin(), numbs.end());
    return result = std::to_string(numbs.back()) + " " + std::to_string(numbs.front());
    
}




