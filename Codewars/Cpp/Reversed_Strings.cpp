#include <string>

std::string reverse_words(const std::string& str) 
{
    std::string result {str.rbegin(), str.rend()};
    return result;
    
}