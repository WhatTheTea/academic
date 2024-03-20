#ifndef WTT_GROUP_H
#define WTT_GROUP_H

#include <vector>
#include <functional>

#include "Student.h"

struct Group {
  std::vector<Student> students;

  Student &Search(std::function<bool(Student)> predicate);

  void Add(Student student);
  void Remove(int id);
  std::vector<Student> getStudentsMeanAsc();
  std::vector<Student> getStudentsMeanDesc();
};

#endif // !WTT_GROUP_H
