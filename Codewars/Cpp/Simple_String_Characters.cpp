#include <string>
#include <regex>
#include <vector>
#include <iostream>

std::vector<int> solve(std::string s){
    
    int upper_case {0};
    int lower_case {0};
    int numbers {0};
    int special {0};
    std::vector<int> result = {upper_case, lower_case, numbers, special};

    for(int i = 0; i < s.size(); ++i)
    {
        if(isdigit(s[i]))
        {
            result[2]++;
        }
        else if(isalpha(s[i]))
        {
            if(islower(s[i]))
            {
                result[1]++;
            }
            else if(isupper(s[i]))
            {
                result[0]++;
            }
        }
        else
        {
            result[3]++;
        }
    }

    return result;
}




int main(){

    std::string s1 = "Codewars@codewars123.com";
    std::vector<int> r = solve(s1);
    for(int i : r)
    {
        std::cout << i << std::endl;
    }

}