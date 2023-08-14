#include <cstring>
#include <string>

bool isvowel(char ch)
{
    ch = std::tolower(ch);
	return (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u');
}

std::string disemvowel(const std::string& str) {
    std::string result;

    for(int i = 0; i < str.length(); ++i)
    {
        if(!isvowel(str[i]))
        {
            result += str[i];
        }
    }
    return result;

}
