#include <iostream>
#include <vector>

unsigned long long factorial(int n)
{
    unsigned long long fact {1};
    if(n == 0 || n == 1)
    {
        return 1;
    }
    for(int i = 1; i <= n; ++i)
    {
        fact *= i;
    }
    return fact;

}


unsigned long long int sum_factorial(std::vector<int> vi)
{
    unsigned long long result {0};
    for(auto element : vi)
    {
        result += factorial(element);
    }
    return result;
}

int main(){

    std::vector<int> v = {4, 6};
    std::cout << sum_factorial(v);

    return 0;
}

