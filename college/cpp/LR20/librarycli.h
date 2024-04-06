#ifndef LIBRARYCLI_H
#define LIBRARYCLI_H

#include "library.h"
class LibraryCLI
{
public:
    LibraryCLI();

    void mainloop();

private:
    Library library;
    void PrintBook(const Book &book);
    void ByIdAndCount();
    void ByName();
    void AddBook();
    void RemoveBook();

    enum Menu
    {
        byIdAndCount = 1,
        byName = 2,
        addBook = 3,
        removeBook = 4,
        exit = 5,
    };
};

#endif // LIBRARYCLI_H
