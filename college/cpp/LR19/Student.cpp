#include "Student.h"
#include <numeric>
#include <sstream>
#include <string>

std::string Student::getInitials() {
  return last_name + " " + name[0] + ". " + patronymic[0] + ". ";
}

std::string Student::toString() {
  std::stringstream s;
  s << this->getInitials() << "Оцінки: ";
  for (auto var : this->grades) {
      s << var << " ";
  }
  s << '\n';
  s << "Середнє арифметичне: " << this->getMean() << '\n';
  return s.str();
}

double Student::getMean()
{
    double sum = std::accumulate(this->grades.begin(), this->grades.end(), 0.0f);
    double count = this->grades.size();
    return sum / count;
}
