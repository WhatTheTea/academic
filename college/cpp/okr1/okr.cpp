#include <iostream>
#define SIZE 5
int main(int argc, char const *argv[])
{
    int nums[SIZE], sum;
    for (size_t i = 0; i < SIZE; i++) std::cin >> nums[i];
    for (auto &&n : nums) sum += n;
    std::cout << (sum / SIZE) << std::endl;
    
    return 0;
}
