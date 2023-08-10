#include <string>


int getCount(const std::string& inputStr){
    int num_vowels = 0;
    for(int i = 0; i < inputStr.length(); ++i)
    {
        if(inputStr[i] == 'a' || inputStr[i] == 'e' || inputStr[i] == 'i' || inputStr[i] == 'o' || inputStr[i] == 'u')
        {
            num_vowels++;
        }
    }
  return num_vowels;
}
