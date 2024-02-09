#include <iostream>
using std::cout, std::cin;
int main(int argc, char const *argv[])
{
    int num = 0;
    cin >> num;
    if (num < 1 && num > 9) return -1;
    for (int i = 1; i <= num; i++)
    {
        for (int j = 1; j <= i; j++)
        {
            cout << j << " ";
        }
        cout << '\n';
    }
    
    return 0;
}
