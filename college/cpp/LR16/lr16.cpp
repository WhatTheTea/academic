#include <functional>
#include <iostream>
#include <string>
#include <vector>

struct Range 
{ 
    int start; 
    int end; 

    bool InRange(int n)
    {
        return n >= start && n <= end;
    }    
};

struct Book
{
    int id;
    std::string title;
    int copies;
};

template<typename T>
T null = {};

struct BookStore
{
    std::vector<Book> books;

    Book& Search(std::function<bool(Book)> predicate)
    {
        for(auto &&book : books)
        {
            if (predicate(book)) return book;
        }
        return null<Book>;
    }

    Book& SearchByIdRange(Range range)
    {
        return Search([&range] (Book b) { return range.InRange(b.id); });
    }
    Book& SearchByCopiesRange(Range range)
    {
        return Search([&range] (Book b) { return range.InRange(b.copies); });
    }
    Book& SearchByName(std::string title)
    {
        return Search([title] (Book b) { return b.title == title; });
    }
};
enum Menu
{
    ByIdRange = 1,
    ByCopiesRange = 2,
    ByName = 3,
    AddBook = 4,
    RemoveBook = 5
};

using std::cout, std::cin, std::string, std::vector;

int main(int argc, const char** argv)
{
    string input;
    int choice;
    while (cin >> input) {
        cout << "Меню:\n\t1. Шукати за номером \n\t2. Шукати за кількістю примірників"
        << "\n\t3. Пошук за іменем\n\t4. Додати книжку\n\t5. Видалити книжку\n";
        if (input == "/exit") break;
        choice = std::stoi(input);
        switch (input[0]) {
            case ByIdRange:
            break;
            case ByCopiesRange:
            break;
            case ByName:
            break;
            case AddBook:
            break;
            case RemoveBook:
            break;
        }
    }

    return 0;
}