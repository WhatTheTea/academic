#include "librarycli.h"
#include "range.h"
#include <iostream>

LibraryCLI::LibraryCLI() {}

void LibraryCLI::PrintBook(const Book &book)
{
    std::cout << "Книга: " << book.getTitle()
              << "\n\tКількість примірників: " << book.getCount()
              << "\n\tІдентифікаційний номер: " << book.getId()
              << "\n";
}

void LibraryCLI::ByIdAndCount()
{
    std::cout << "Введіть діапазон ідентифікаційних номерів: \nВід До: ";
    int start = 0, end = 0;
    std::cin >> start >> end;
    std::cout << "Введіть максимальну кількість примірників: \nДо: ";
    int max_count = 0;
    std::cin >> max_count;
    auto book = this->library
                    .FindIdsInRangeAndCountLessThan(Range(start, end), max_count);
    this->PrintBook(*book);
}

void LibraryCLI::ByName()
{
    std::cout << "Введіть ім'я книги:";
    std::string title;
    std::cin >> title;
    auto book = this->library.FindTitle(title);
    this->PrintBook(*book);
}

void LibraryCLI::AddBook()
{
    std::string title;
    int id = 0, count = 0;
    std::cout << "Введіть назву книги: ";
    std::cin >> title;
    std::cout << "Введіть номер книги: ";
    std::cin >> id;
    std::cout << "Введіть кількість примірників : ";
    std::cin >> count;
    this->library.Add(Book(title,id,count));
    std::cout << "Книгу додано!\n";
}

void LibraryCLI::RemoveBook()
{
    std::cout << "Введіть номер книги за порядком: ";
    int id = 0;
    std::cin >> id;
    this->library.Remove(id);
    std::cout << "Книгу видалено!\n";
}

void LibraryCLI::mainloop()
{
    int choice;
    bool running = true;
    while (running) {
        std::cout << "Меню:\n\t1. Шукати за номером та кількістю"
             << "\n\t2. Пошук за іменем\n\t3. Додати книжку\n\t4. Видалити книжку"
                  << "\n\t5. Вихід\n> ";
        std::cin >> choice;
        switch (choice) {
        case byIdAndCount:
            this->ByIdAndCount();
            break;
        case byName:
            this->ByName();
            break;
        case addBook:
            this->AddBook();
            break;
        case removeBook:
            this->RemoveBook();
            break;
        default:
        case exit:
            running = false;
            break;
        }
    }
}
