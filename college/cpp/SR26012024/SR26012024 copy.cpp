#include <cmath>
#include <iostream>
#include <string>

using namespace std;

float var5(float n) 
{
	float up = pow(n,3) + 5*2*2 - 7*n + 14 + 2*cos(n);
	float down = pow(n,5) + 2*pow(n,3) - 4*n + 11;
	if (down != 0) return up/down;
	throw -1;
}

int main()
{
	for (int i = 0; i < 3; i++)
	{
		cout << var5(i) << '\n';
	}
}