#ifndef BOOK_H
#define BOOK_H

#include <string>


class Book
{
public:
    Book(const std::string &title, const int &id, const int &count);

    std::string getTitle() const;
    int getId() const;
    int getCount() const;
protected:
    void setTitle(const std::string &newTitle);
    void setId(const int &newId);
    void setCount(const int &newCount);
private:
    std::string title;
    int id;
    int count;
};

#endif // BOOK_H
