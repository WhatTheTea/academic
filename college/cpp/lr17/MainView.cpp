#include "MainView.h"

#include <iostream>
#include <string>

using std::cin, std::cout, std::string;

void studentConsoleView::AddStudent() {
  auto new_student = null<Student>;
  cout << "Введіть ПІБ: ";
  cin >> new_student.last_name >> new_student.name >> new_student.patronymic;
  cout << "Введіть оцінку за перший, потім за другий семестр: ";
  cin >> new_student.firstMean >> new_student.secondMean;
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

void studentConsoleView::PrintAll() {
  cout << "Всі студенти: \n";
  for (auto &s : group.students) {
    cout << s.toString() << '\n';
  }
}

void studentConsoleView::SearchSameSecondMean() {
  cout << "Студенти з однаковою оцінкою за 2 семестр:\n";
  auto studs = group.SearchSameSecondMean();
  for (auto stud : studs) {
    cout << stud.toString() << '\n';
  }
}

void studentConsoleView::mainloop() {
  string input;
  int choice;
  studentConsoleView view;
  while (true) {
    cout << "Меню:\n\t1.Однакові середні бали \n\t2. Всі"
         << "\n\t3. Додати\n\t4. Видалити\n";
    cin >> input;
    if (input == "/exit")
      break;

    switch (std::stoi(input)) {
    case Menu::AddStudent:
      view.AddStudent();
      break;
    case Menu::RemoveStudent:
      view.RemoveStudent();
      break;
    case Menu::PrintEveryone:
      view.PrintAll();
      break;
    case Menu::SameMean:
      view.SearchSameSecondMean();
      break;
    }
  }
}