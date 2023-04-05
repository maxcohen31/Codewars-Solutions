#include <iostream>
#include <vector>
#include <algorithm>

int sum_even_numbers(const std::vector<double> &seq) {
    int result {0};
    for(auto ele: seq)
    {
        if(static_cast<int>(ele) == ele && static_cast<int>(ele) % 2 == 0)
        {
            result += ele;
        }
    }
    return result;
}

int main(){


    std::vector<double> vec {2.0, 2.3, 2, 5, 6};
    std::cout << sum_even_numbers(vec);
    return 0;
}