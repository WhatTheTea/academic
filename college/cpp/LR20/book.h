#ifndef BOOK_H
#define BOOK_H

#include <string>


class Book
{
public:
    Book(const std::string &title, const std::string &id, const int &count);

    std::string getTitle() const;
    std::string getId() const;
    int getCount() const;

protected:
    std::string title;
    std::string id;
    int count;
    void setTitle(const std::string &newTitle);
    void setId(const std::string &newId);
    void setCount(int newCount);
};

#endif // BOOK_H
