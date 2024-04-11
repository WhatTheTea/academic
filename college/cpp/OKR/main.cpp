#include <array>
#include <iostream>

int max(std::array<int, 10> &arr){
    int max = INT_MIN;
    for (auto &i : arr) {
        if(i > max) max = i;
    }
    return max;
}
int min(std::array<int, 10> &arr){
    int min = INT_MAX;
    for (auto &i : arr) {
        if(i < min) min = i;
    }
    return min;
}
void populate(std::array<int, 10> &nums)
{
    for (int var = 0; var < 10; var++) {
        int input = 0;
        std::cin >> input;
        nums[var] = input;
    }
}

int main()
{
    std::array<int, 10> nums;
    populate(nums);
    std::cout << "\nМаксимальне: " << max(nums) << '\n'
              << "Мінімальне: " << min(nums) << '\n';
    return 0;
}
