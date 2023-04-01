#include <stack>
#include <string>
#include <iostream>

bool validParentheses(const std::string& str) {
    std::stack<char> parentheses;

    for(int i = 0; i < str.length(); ++i)
    {   
        if(str[i] == '(' || str[i] == '[' || str[i] == '{')
        {
            parentheses.push(str[i]);
        }
        else if(str[i] == ')' || str[i] == ']' || str[i] == '}')
        {
            if(parentheses.empty())
            {
                return false;    
            }
            else if(str[i] == ')' && parentheses.top() != '(')
            {
                return false;
            }
            else if(str[i] == ']' && parentheses.top() != '[')
            {
                return false;
            }
            else if(str[i] == '}' && parentheses.top() != '{')
            {
                return false;
            }
            else
            {
                parentheses.pop();
            }
        }
    }
    if(parentheses.size() == 0){
        return true;
    }
    else
    {
        return false;
    } 
}


int main(){

    std::string p {"()[]{}"};
    std::string p1 {"(]"};
    std::cout << std::boolalpha << validParentheses(p1) << std::endl;

    return 0;
}