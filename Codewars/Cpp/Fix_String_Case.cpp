#include <string>
#include <iostream>

std::string solve(const std::string& str){

    std::string new_str = str;
    int lower_case {0};
    int upper_case {0};
    std::string result;

    for(int i {0}; i < new_str.length(); ++i)
    {
        if(islower(new_str[i]))
        {
            lower_case++;
        }
        else
        {
            upper_case++;
        }
    }
    if(lower_case < upper_case)
    {
        for(char c: new_str)
        {
            result += toupper(c);
        }
    }
    else if(lower_case >= upper_case)
    {
        for(char c: new_str)
        {
            result += tolower(c);
        }
    }
    return result;
}


int main(){

    std::string s = "CODe";
    std::cout << solve(s);


    return 0;
}