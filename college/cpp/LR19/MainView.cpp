#include "MainView.h"
#include "Null.h"

#include <iostream>
#include <string>

using std::cin, std::cout, std::string;

void studentConsoleView::AddStudent() {
  auto new_student = null<Student>;
  cout << "Введіть ПІБ: ";
  cin >> new_student.last_name >> new_student.name >> new_student.patronymic;
  cout << "Введіть оцінки з трьох предметів: ";
  for (auto &grade : new_student.grades) {
      cin >> grade;
  }
  group.Add(new_student);
  cout << "Студента додано!\n";
}

void studentConsoleView::RemoveStudent() {
  cout << "Введіть номер студента:";
  int id = 0;
  cin >> id;
  group.Remove(id);
  cout << "Студента видалено!\n";
}

void studentConsoleView::PrintAllMeanAscending() {
  cout << "Всі студенти за зростаючим середнім балом: \n";
  for (auto &s : this->group.getStudentsMeanAsc()) {
    cout << s.toString() << '\n';
  }
}

void studentConsoleView::PrintAllMeanDescending() {
    cout << "Всі студенти за спадаючим середнім балом: \n";
    for (auto &s : this->group.getStudentsMeanDesc()) {
        cout << s.toString() << '\n';
    }
}

void studentConsoleView::mainloop() {
  string input;
  int choice;
  while (true) {
    cout << "Меню:\n\t1. Спадаючі середні бали \n\t2. Зростаючі середні бали"
         << "\n\t3. Додати\n\t4. Видалити\n";
    cin >> input;
    if (input == "/exit")
      break;

    switch (std::stoi(input)) {
    case Menu::AddStudent:
        this->AddStudent();
      break;
    case Menu::RemoveStudent:
        this->RemoveStudent();
      break;
    case Menu::PrintAllMeanAsc:
        this->PrintAllMeanAscending();
      break;
    case Menu::PrintAllMeanDesc:
        this->PrintAllMeanDescending();
        break;
    }
  }
}
