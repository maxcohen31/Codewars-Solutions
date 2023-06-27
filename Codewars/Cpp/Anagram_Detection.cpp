#include <algorithm>
#include <string>

bool isAnagram(std::string test, std::string original)
{
    int length_test = test.length();
    int length_original = original.length();
        
    // To lowercase
    std::transform(test.begin(), test.end(), test.begin() , ::tolower);
    std::transform(original.begin(), original.end(), original.begin() ,::tolower);

    std::sort(test.begin(), test.end());
    std::sort(original.begin(), original.end());
    
    if(length_test != length_original)
    {
        return false;
    }

    for (int i = 0; i < length_original; ++i)
    {
        if(test[i] != original[i])
        {
            return false;
        }

    }
    return true; 
}
