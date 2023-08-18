#include <string>
#include <map>
#include <functional>

bool am_i_afraid(const std::string &day, int num)
{
    if(day == "Monday" && num == 12)
    {
        return true;
    }
    else if (day == "Tuesday" && num > 95) 
    {
        return true;
    }
    else if (day == "Wednesday" && num == 34) 
    {
        return true;
    }
    else if (day == "Thursday" && num == 0)
    {
    return true;
    }
    else if (day == "Friday" && num % 2 == 0) 
    {
        return true;
    }
    else if (day == "Saturday" && num == 56) 
    {
        return true;
    }
    else if( day == "Sunday" && (num == 666 || num == -666))
    {
        return true;
    }
    else 
    {
        return false;
    }
    
}

// Clever Solution
bool am_i_afraid(const std::string &day, int num)
{
  std::map<std::string, std::function<bool(int)>> mapping
  {
    {"Monday",    [](int num){return num == 12;}},
    {"Tuesday",   [](int num){return num > 95;}},
    {"Wednesday", [](int num){return num == 34;}},
    {"Thursday",  [](int num){return num == 0;}},
    {"Friday",    [](int num){return num % 2 == 0;}},
    {"Saturday",  [](int num){return num == 56;}},
    {"Sunday",    [](int num){return (num == 666) || (num == -666);}}
  };
  
  return mapping[day](num);
}
