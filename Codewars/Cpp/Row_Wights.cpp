#include <vector>
#include <utility>
 

std::pair<int, int> rowWeights (const std::vector<int> &weights)
{
    std::pair<int, int> result;

    for(int i = 0; i < weights.size(); ++i)
    {
        if(i % 2 == 0)
        {
            result.first += weights[i];
        }
        else
        {
            result.second += weights[i];
        }
    }
    return result;
}