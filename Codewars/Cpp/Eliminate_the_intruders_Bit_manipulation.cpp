#include <algorithm>
#include <iostream>
#include <cmath>

long eliminate_unset_bits(std::string number){
    std::string n = number;
    n.erase(std::remove(n.begin(), n.end(), '0'), n.end());

    int counter {0};
    long result {0};
    
    for(int i = n.size() - 1; i >= 0; --i)
    {
        result += std::pow(2, i);
        counter++;
    }
    return result;

}


int main(){

    std::string my_str {"11010101010101"};
    std::string my_str2 {"00"};
    std::cout << eliminate_unset_bits(my_str2);
    return 0;
}
