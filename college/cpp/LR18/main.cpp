#include <iostream>
#include <fstream>
#include <vector>
#include "sourcefiles.h"

void writeRandomNumbers(sourceFiles files)
{
    for (int i = 0; i < 10; i++) {
        files.f << rand() % 100 << '\n';
        files.g << rand() % 100 << '\n';
        files.k << rand() % 100 << '\n';
    }
}

std::vector<int> readNumbersFrom(std::fstream &file)
{
    std::vector<int> result;
    std::string buffer;
    while (std::getline(file, buffer) && buffer != "")
    {
        result.push_back(std::stoi(buffer));
    }
    file.seekg(0);
    return result;
}

int main()
{
    std::fstream file_f("f.txt"), file_g("g.txt"), file_k("k.txt");
    auto files = sourceFiles{file_f, file_g, file_k};
    srand(time(nullptr));
    writeRandomNumbers(files);
    files.flushAll();

    auto n_f = readNumbersFrom(files.f);
    auto n_g = readNumbersFrom(files.g);
    auto n_k = readNumbersFrom(files.k);

    std::vector<int> results;

    for (int i = 0; i < n_f.size(); i++) {
        results.push_back(n_f[i] * n_g[i] * n_k[i]);
    }
    std::ofstream output("c.txt");
    for (auto x : results) {
        output << x << '\n';
    }
    files.closeAll();
    output.close();
    return 0;
}
