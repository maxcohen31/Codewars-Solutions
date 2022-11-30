#include <iostream>
#include <cmath>

bool isPrime(int num) {
    int first_prime = 2;
    
    if(num <= 1)
    {
        return false;
    }
    while(first_prime < std::sqrt(num))
    {
        if(num % first_prime == 0)
        {
            return false;
        }
        first_prime++;
    }
    return true;
}

int main(){


    int n = 11;
    std::cout << isPrime(n); 
    return 0;
}