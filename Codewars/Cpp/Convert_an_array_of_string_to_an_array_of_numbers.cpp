#include <vector>
#include <string>

std::vector<float> to_float_array(const std::vector<std::string>& arr) {
    
    std::vector<std::string> new_arr = arr; 
    std::vector<float> result;

    for(int i = 0; i < size(new_arr); ++i)
    {
        result.push_back(std::stof(new_arr[i]));
    }
    return result;
}

