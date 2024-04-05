#include "book.h"

Book::Book() {}

std::string Book::getTitle() const
{
    return title;
}

void Book::setTitle(const std::string &newTitle)
{
    title = newTitle;
}

std::string Book::getId() const
{
    return id;
}

void Book::setId(const std::string &newId)
{
    id = newId;
}

int Book::getCount() const
{
    return count;
}
