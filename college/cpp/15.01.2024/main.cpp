#include <iostream>
#include <map>
#include <tuple>
using std::cout, std::string, std::map, std::tuple;
bool isGood(int m, int u, int e, int p, int h)
{
    int mean = (m+u+e+p+h)/5;
    return mean > 3;
}
int main(int argc, char const *argv[])
{
    map<string, tuple<int,int,int,int,int>> grades = {
        {"Student1", {1,2,3,4,5}},
        {"Student2", {3,4,4,3,4}},
        {"Student3", {5,4,4,4,5}},
        {"Student4", {3,4,4,5,5}}
    };
    for (auto g : grades){
        auto[m,u,e,p,h] = g.second;
        cout << g.first << " " << (isGood(m,u,e,p,h) ? "Хорошист" : "Не хорошист") << '\n';
    }
    return 0;
}
