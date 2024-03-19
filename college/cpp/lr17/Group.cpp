#include "Group.h"

Student &Group::Search(std::function<bool(Student)> predicate) {
    for (auto &&student : students) {
      if (predicate(student))
        return student;
    }
    return null<Student>;
  }

std::array<Student, 2> Group::SearchSameSecondMean()
  {
    auto second = null<Student>;
    auto student = Search([&second, this](Student s)
    {
      second = Search([&s](Student sec){return s.secondMean == sec.secondMean && s.getInitials() != sec.getInitials();});
      return s.secondMean == second.secondMean;
    });
    auto students = std::array<Student, 2>{student, second};
    return students;
  }

void Group::Add(Student book) { students.push_back(book); }
void Group::Remove(int id) { students.erase(students.begin() + id); }