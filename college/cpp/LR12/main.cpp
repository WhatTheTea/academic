#include <iostream>
#include <string>
#include <numeric>
using std::cout, std::cin, std::string;

int size = 8, length = 0;

auto make_array() {
	string input;
	auto arr = new int[size];
	while (cin >> input && input != "end")
	{
		arr[length] = std::stoi(input);
		if (length >= size - 1) {
			auto arr2 = new int[size *= 2];
			memcpy(arr2, arr, length*sizeof(arr));
			arr = arr2;
		}
		length++;
	}
	return arr;
}

int main()
{	
	auto array = make_array();
	int sum = 0;
	sum = std::accumulate(array, array + length, sum);
	cout << sum;
	delete[] array;
	return 0;
}