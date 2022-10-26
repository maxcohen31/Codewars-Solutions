#include <vector>
#include<iostream>
#include<algorithm>
using namespace std;

int sumOfDifference(const vector<int>& arr){
    
    int result {0};
    vector<int> new_vector = arr;
    sort(new_vector.begin(), new_vector.end(), greater<int>());

    for(int i = 0; i < size(new_vector) - 1; ++i)
    {
        result += new_vector[i] - new_vector[i+1];
    }
    return result;
}

int main(){

    vector<int> arr1 {2, 1, 10};

    cout << sumOfDifference(arr1) << endl;

    return 0;
}