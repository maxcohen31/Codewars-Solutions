#include <iterator>
#include <string>
#include <iostream>
#include <algorithm>

bool solution(std::string const &str, std::string const &ending) 
{
    if(ending == "")
    {
        return true;
    }
    return std::equal(ending.rbegin(), ending.rend(), str.rbegin());

}


int main(){

    std::string s1 {"abcde"};
    std::string s2 {"cde"};
    std::cout << solution(s1, s2);
    return 0;
}
