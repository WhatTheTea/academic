#include <iostream>
#include <math.h>
#include <string>

static inline void expr(float n) 
{
	float res = (n * sin(n) / n * sin(n) + 5 * n + 4);
	std::cout << (isnan(res) ? "error" : std::to_string(res))
			  << '\n';
}

int main()
{
	for (int i = 1; i <= 5; expr(i++));
}