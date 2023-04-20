#include <iostream>
#include <string>

std::string pattern(int n)
{   
    std::string result;
    
    if(n <= 1) { return ""; }

    for(int i = 1; i <= n; ++i)
    {     
        result += "\n";
        for(int j = 1; j <= i; ++j)
        {   
            result += std::to_string(i);
        }
    }
    return result.substr(1, result.length());
}


int main(){

    std::cout << pattern(4);
    return 0;
}