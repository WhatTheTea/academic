#include <iostream>
#include <math.h>

int main(){
    int x = 0;
    std::cin >> x;
    float znam = sqrt(1+exp(-x));
    if (znam == 0) {
        std::cout << "Знаменник менше нуля\n";
        return -1;
    }
    float res = 1/znam;
    std::cout << res << "\n";
}