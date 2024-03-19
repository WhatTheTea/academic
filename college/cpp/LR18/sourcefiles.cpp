#include "sourcefiles.h"
void sourceFiles::flushAll()
{
    f.flush();
    g.flush();
    k.flush();
    f.seekp(0);
    g.seekp(0);
    k.seekp(0);
}

void sourceFiles::closeAll()
{
    f.close();
    g.close();
    k.close();
}
