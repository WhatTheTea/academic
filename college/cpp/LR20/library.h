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
    std::vector<Book>::const_iterator end() { return books.cend(); }

    std::vector<Book&> FindIdsInRangeAndCountLessThan(Range range, int maxCount);
    std::vector<Book&> FindTitle(const std::string &title);

protected:
    std::vector<Book> books;
};

#endif // LIBRARY_H
