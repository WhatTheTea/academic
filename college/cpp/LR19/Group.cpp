#include "Group.h"
#include "Null.h"

Student &Group::Search(std::function<bool(Student)> predicate) {
    for (auto &&student : students) {
      if (predicate(student))
        return student;
    }
    return null<Student>;
  }

void Group::Add(Student student) { students.push_back(student); }
void Group::Remove(int id) { students.erase(students.begin() + id); }
std::vector<Student> Group::getStudentsMeanAsc()
{
    auto result = this->students;
    std::sort(result.begin(), result.end(), [](Student x, Student y){
        return x.getMean() > y.getMean();
    });
    return result;
}

std::vector<Student> Group::getStudentsMeanDesc()
{
    auto result = this->students;
    std::sort(result.begin(), result.end(), [](Student x, Student y){
        return x.getMean() < y.getMean();
    });
    return result;
}
