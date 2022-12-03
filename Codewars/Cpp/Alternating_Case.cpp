#include <string>
#include <iostream>


std::string to_alternating_case(const std::string& str)
{
	std::string result;
    for(size_t i {0}; i < str.length(); ++i)
    {
        if(islower(str[i]))
        {
            result += toupper(str[i]);
        }
        else
        {
            result += tolower(str[i]);
        }
    }
    return result;
}


int main(){

    std::string s1 = "hello world";
    std::string s2 = "HeLLo WoRlD";

    std::cout << to_alternating_case(s1);
    return 0;
}