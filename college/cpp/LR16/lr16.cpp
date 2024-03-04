#include <functional>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using std::cout, std::cin, std::string;

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

    std::string toString()
    {
        std::stringstream s;
        s << title << ": ID: " << id << "Copies: " << copies;
        return s.str();
    }
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
    void Add(Book book)
    {
        books.push_back(book);
    }
    void Remove(int id)
    {
        std::vector<Book> new_books;
        for (auto book : books) {
            if(book.id != id) new_books.push_back(book);
        } 
        books = new_books;
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
struct BookStoreConsoleView
{
    BookStore bookstore;

    BookStoreConsoleView()
    {
        bookstore = BookStore();
    }

    void ById()
    {
        cout << "Введіть діапазон ідентифікаційних номерів: \nВід До: ";
        Range range;
        cin >> range.start >> range.end;
        auto book = bookstore.SearchByIdRange(range);
        cout << book.toString() << '\n';
    }

    void ByCopies()
    {
        cout << "Введіть діапазон кількості примірників: \nВід До: ";
        Range range;
        cin >> range.start >> range.end;
        auto book = bookstore.SearchByCopiesRange(range);
        cout << book.toString() << '\n';
    }

    void ByName()
    {
        cout << "Введіть ім'я книги:";
        string name;
        cin >> name;
        auto book = bookstore.SearchByName(name);
        cout << book.toString() << '\n';
    }

    void AddBook()
    {
        auto new_book = null<Book>;
        cout << "Введіть назву книги: ";
        cin >> new_book.title;
        cout << "Введіть номер книги: ";
        cin >> new_book.id;
        cout << "Введіть кількість примірників : ";
        cin >> new_book.copies;
        bookstore.Add(new_book);
        cout << "Книгу додано!\n";
    }

    void RemoveBook()
    {
        cout << "Введіть номер книги:";
        int id = 0;
        cin >> id;
        bookstore.Remove(id);
        cout << "Книгу видалено!\n";
    }

    void mainloop()
    {
        string input;
        int choice;
        while (true) {
            cout << "Меню:\n\t1. Шукати за номером \n\t2. Шукати за кількістю примірників"
            << "\n\t3. Пошук за іменем\n\t4. Додати книжку\n\t5. Видалити книжку\n";
            cin >> input;
            if (input == "/exit") break;

            switch (std::stoi(input)) {
                case Menu::ByIdRange: 
                    ById();
                    break;
                case Menu::ByCopiesRange: 
                    ByCopies();
                    break;
                case Menu::ByName: 
                    ByName();
                    break;
                case Menu::AddBook: 
                    AddBook();
                    break;
                case Menu::RemoveBook: 
                    RemoveBook();
                    break;
            }
        }
    }
};


int main(int argc, const char** argv)
{
    auto bookstoreView = BookStoreConsoleView();
    bookstoreView.mainloop();
    return 0;
}