#ifndef WTT_STUDENT_H
#define WTT_STUDENT_H

#include <string>

struct Student {
  double firstMean;
  double secondMean;
  std::string name;
  std::string last_name;
  std::string patronymic;

  std::string getInitials();

  std::string toString();
};
#endif // !WTT_STUDENT_H