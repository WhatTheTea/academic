#ifndef WTT_GROUP_H
#define WTT_GROUP_H

#include <vector>
#include <array>
#include <functional>

#include "Student.h"
#include "Null.h"

struct Group {
  std::vector<Student> students;

  Student &Search(std::function<bool(Student)> predicate);

  std::array<Student, 2> SearchSameSecondMean();

  void Add(Student student);
  void Remove(int id);
};

#endif // !WTT_GROUP_H