#ifndef WTT_STUDENT_H
#define WTT_STUDENT_H

#include <array>
#include <string>

struct Student {
  std::array<double, 3> grades;

  std::string name;
  std::string last_name;
  std::string patronymic;

  std::string getInitials();
  std::string toString();
  double getMean();
};
#endif // !WTT_STUDENT_H
