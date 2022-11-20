#include <vector>
#include <iostream>

std::vector<int> invert(std::vector<int> values)
{
    for(int i = 0; i < values.size(); ++i)
    {
        if(values[i] < 0)
        {
            values[i] = -1 * values[i];
        }
        else if(values[i] > 0)
        {
            values[i] = -1 * values[i];
        }
    }
    return values;
}


int main(){

    std::vector<int> v {1, -2, 3, -4, 5};
    std::vector<int> new_vec = invert(v);
    for(int integer : new_vec)
    {
        std::cout << integer << std::endl;
    }
    return 0;
}