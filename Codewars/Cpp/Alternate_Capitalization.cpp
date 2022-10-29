#include <string>
#include <utility>

std::pair<std::string, std::string> capitalize(const std::string &s)
{
    std::string new_str = s;
    std::string result1;
    std::string result2;

    for(int i = 0; i < new_str.length(); ++i)
    {
        if(i % 2 == 0)
        {
          result1 += toupper(new_str[i]);
        }
      else
      {
          result1 += new_str[i];
      }
    }
    
    for(int i = 0; i < new_str.length(); ++i)
    {
        if(i % 2 != 0)
        {
          result2 += toupper(new_str[i]);
        }
      else
      {
          result2 += new_str[i];
      }
    }
    return {result1, result2};
}