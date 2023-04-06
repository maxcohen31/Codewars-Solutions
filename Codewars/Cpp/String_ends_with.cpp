#include <string>
#include <iostream>

bool solution(std::string const &str, std::string const &ending) 
{   
    if(ending == "") { return true; }
    else if(str.length() < ending.length()) { return false; }
    return str.substr(str.length() - ending.length(), str.length()) == ending ? true : false;
}
