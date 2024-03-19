#include "Student.h"
#include <string>
#include <sstream>

std::string Student::getInitials() { return last_name + " " + name[0]+ ". " + patronymic[0] + ". "; }

std::string Student::toString() {
std::stringstream s;
s << getInitials() << ":\n"
    << "Середня оцінка за 1 семестр: " << firstMean << "\n"
    << "Середня оцінка за 2 семестр: " << secondMean << '\n';
return s.str();
}