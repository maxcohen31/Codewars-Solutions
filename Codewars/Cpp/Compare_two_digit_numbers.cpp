#include <string>
#include <iostream>
#include <algorithm>

std::string compare(unsigned short a, unsigned short b)
{
    std::string str_a = std::to_string(a);
    std::string str_b = std::to_string(b);
    std::string str_intersection;

    // Intersection 
    std::sort(str_a.begin(), str_a.end());
    std::sort(str_b.begin(), str_b.end());
    std::set_intersection(str_a.begin(), str_a.end(), str_b.begin(), str_b.end(), std::back_inserter(str_intersection));
    if(str_intersection.length() == 2) { return "100%"; }
    else if(str_intersection.length() == 1) { return "50%"; }
    else { return "0%"; }
}

int main(){

    unsigned short a {13};
    unsigned short b {14};
    std::cout << compare(a, b);

    return 0;
}