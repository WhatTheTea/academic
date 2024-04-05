#include "library.h"
#include <algorithm>

Library::Library() {}

const Book* Library::FindIdsInRangeAndCountLessThan(const Range &range, int maxCount)
{
    return std::find_if(this->begin(), this->end(), [&](Book b){
               return range.IsInRange(b.getId())
                      && b.getCount() < maxCount;}).base();
}

const Book* Library::FindTitle(const std::string &title)
{
    return std::find_if(this->begin(), this->end(), [&](Book b){
               return b.getTitle() == title;}).base();
}

void Library::Add(const Book &b)
{
    this->books.push_back(b);
}

void Library::Remove(int index)
{
    auto book = this->books.at(index);
    this->books.erase(this->books.begin()+index);
}

