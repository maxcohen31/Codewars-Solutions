#include <vector>
#include <algorithm>
#include <iostream>

int betweenExtremes(const std::vector<int>& numbers)
{
    int max = *std::max_element(numbers.begin(), numbers.end());
    int min = *std::min_element(numbers.begin(), numbers.end());
    return max - min;
}



int main(){

    std::vector<int> v = {1, 434, 555, 34, 112};
    std::cout << betweenExtremes(v);

    return 0;
}