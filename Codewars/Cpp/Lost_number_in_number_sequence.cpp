#include <iostream>
#include <list>
#include <numeric>

int findDeletedNumber(std::list<int> startingList, std::list<int> mixedList)
{
    int startingListSum {0};
    int mixedListSum {0};
    
    return std::accumulate(startingList.begin(), startingList.end(), startingListSum) - std::accumulate(mixedList.begin(), mixedList.end(), mixedListSum);

}



int main(){
    
    std::list<int> l {1, 2, 3, 4, 5, 6, 7, 8, 9};
    std::list<int> l2 {1, 2, 3, 4, 6, 7, 8, 9};
    int result = findDeletedNumber(l, l2);
    
    std::cout << result;

    return 0;
}
