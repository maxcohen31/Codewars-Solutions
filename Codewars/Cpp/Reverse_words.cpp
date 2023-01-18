#include <string>
#include <algorithm>
std::string reverse_words(std::string str) 
{
    int j {0}; // left
    int k {0}; // right
    while(j < str.length())
    {
        while(k < str.length() && str[k] != ' ')
        {
            k++;
        }
        std::reverse(str.begin() + j, str.begin() + k);
        j = k + 1;
        k = j;
    }
    return str;

}


