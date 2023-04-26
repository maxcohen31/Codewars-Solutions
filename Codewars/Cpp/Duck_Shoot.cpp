#include <string>
#include <iostream>
#include <cmath>

std::string duckShoot(int ammo, double aim, std::string ducks){
    unsigned int hitDucks = floor(aim * ammo);
    
    for(int i = 0; i < ducks.size(); ++i)
    {
        if(ducks[i] == '2' && hitDucks > 0)
        {
            ducks[i] = 'X';
            hitDucks--;
        }
    }
    return ducks;
}


int main(){

    std::cout << duckShoot(4, 0.64, "|~~2~~~22~2~~22~2~~~~2~~~|");
    std::cout << floor(4 * 0.64);
    std::cout << floor(8 * 0.05);
    return 0;
}