#ifndef SOURCEFILES_H
#define SOURCEFILES_H

#include <fstream>


struct sourceFiles
{
    std::fstream &f;
    std::fstream &g;
    std::fstream &k;

    void flushAll();
    void closeAll();
};

#endif // SOURCEFILES_H
