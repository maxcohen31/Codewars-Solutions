#include <string>
#include <iostream>
#include <cmath>

int numberLength(int number)
{
    int digits {0};
    while(number)
    {
        number = number / 10;
        digits++;
    }
    return digits;
    
}

std::string disariumNumber(int number)
{   
    int temp = number;
    int result {0};
    int number_digits = numberLength(number);
    while(temp)
    {
        int last_digit = temp % 10;
        result += pow(last_digit, number_digits--);
        temp = temp / 10;
    }
    
    if(result == number) { return "Disarium !!"; }
    else { return "No !!"; }
}

// Alternative Solution
#include <cmath>

std::string disariumNumber(const int num)
{
    unsigned int sum = 0;

    std::string numStr = std::to_string(num);
    for (size_t i = 0; i < numStr.length(); i++)
        sum += pow(std::stoi(std::string (1, numStr[i])), i + 1);

    return sum == num ? "Disarium !!" : "Not !!";
}

int main(){

    std::cout << numberLength(89);
    std::cout << disariumNumber(89);

}