#include "book.h"

Book::Book(const std::string &title, const int &id, const int &count)
{
    this->id = id;
    this->title = title;
    this->count = count;
}

std::string Book::getTitle() const
{
    return title;
}

void Book::setTitle(const std::string &newTitle)
{
    title = newTitle;
}

int Book::getId() const
{
    return id;
}

void Book::setId(const int &newId)
{
    id = newId;
}

int Book::getCount() const
{
    return count;
}

void Book::setCount(const int &newCount)
{
    count = newCount;
}
