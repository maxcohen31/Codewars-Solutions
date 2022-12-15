#include <string>
#include <unordered_map>
#include <iostream>
using namespace std;

unsigned int countConsonants(const std::string& str){
    
    unordered_map<char, int> umap;

    for (int i = 0; i < str.length(); i++) {
        char c = tolower(str[i]);
        if (c != 'a' && c != 'e' && c != 'o' && c != 'u' && c != 'i' &&
            c >= 97 && c <= 122)
        umap[c]++;
    }
    
    return umap.size();
}

int main(){


    int result = countConsonants("aeiou");
    std::cout << result << std::endl;
    return 0;
}