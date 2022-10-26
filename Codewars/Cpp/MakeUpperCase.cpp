#include <string>
using namespace std;

string makeUpperCase (const string& input_str)
{
  string temp = input_str;
  
  for(int i = 0; i < temp.length(); i++)
    {
        temp[i] = toupper(temp[i]);
    } 
  return temp;
}