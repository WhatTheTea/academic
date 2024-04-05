#ifndef LIBRARY_H
#define LIBRARY_H

#include "book.h"
#include "range.h"
#include <vector>

class Library
{
public:
    Library();

    std::vector<Book>::const_iterator begin() const { return books.cbegin(); }
    std::vector<Book>::const_iterator end() const { return books.cend(); }

    const Book* FindIdsInRangeAndCountLessThan(const Range &range, int maxCount);
    const Book* FindTitle(const std::string &title);

    void Add(const Book &b);
    void Remove(int index);

protected:
    std::vector<Book> books;
};

#endif // LIBRARY_H
