#include <vector>

int elevator_distance(std::vector<int> array) 
{
  int result {0};
  for(int i = 1; i < array.size(); ++i)
  {
      result += abs(array[i] - array[i - 1]);
  }
  return result;
}
