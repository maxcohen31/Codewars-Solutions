#include <string>

int factorial(int n)
{
    int result {1};
    if(n == 0 || n == 1) { return 1; }
    for(int i = 1; i <= n; i++)
    {
        result *= i;
    }
    return result;
}

std::string strong_num(int number)
{   
    int temp = number;
    int result {0};
    while(temp > 0)
    {   
        result += factorial(temp % 10);
        temp /= 10;
    }
    if(result == number) 
    { 
        return "STRONG!!!!"; 
    }
    else
    {
        return "No"; 
    }
}
