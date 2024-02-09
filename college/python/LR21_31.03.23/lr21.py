# 6 Юридичний факультет, технічний інститут, гуманітарний факультет
from dataclasses import dataclass
from enum import Enum
from typing import *

# Перелічення статей
class Gender(Enum):
    XX = 0
    XY = 1
# Клас даних студента
@dataclass
class Student:
    first_name : str
    last_name : str
    avg_grade : float
    gender : bool
# Клас даних факультету
class Faculty:
    # Назва
    _name : str
    @property
    def Name(self):
        return self._name
    # Студенти
    _students : List[Student]
    @property
    def Students(self):
        return self._students
    # Конструктор
    def __init__(self, name) -> None:
        self._name = name
        self._students = []
    
    # Інтерфейс взаємодії зі студентами факультету
    def AddStudent(self, student : Student):
        self.Students.append(student)
    def AppendStudents(self, students : Iterable[Student]):
        self.Students.extend(students)
    def RemoveStudent(self, student : Student):
        self.Students.remove(student)
        del student
    # К-сть чоловіків \ жінок
    def CountGender(self, gender : Gender):
        gendered_students = [s for s in self.Students if s.gender == gender]
        return len(gendered_students)
    # Середній бал факультету
    @property
    def AvgGrade(self):
        students = [s.avg_grade for s in self.Students]
        return sum(students) / len(students)
    # К-сть студентів
    @property
    def Count(self):
        return len(self.Students)

jur = Faculty("Юридичний факультет")
hum = Faculty('Гуманітарний факультет')
tech = Faculty("Технічний факультет")

students = [
    Student('Гена','Цидрусні',3.5,Gender.XY),
    Student('Емілія','Вілсон',5,Gender.XX),

    Student('Гюнтер',"О'Дим",5,Gender.XY),
    Student('Геральт','з Рівії',2,Gender.XY),

    Student('Міля','Вуйчич',3,Gender.XX),
    Student('Яна','Цист',4,Gender.XX)
]

jur.AppendStudents(students[0:2])
hum.AppendStudents(students[2:4])
tech.AppendStudents(students[4:7])

for faculty in jur,hum,tech:
    print(f"Середня оцінка в {faculty.Name}: {faculty.AvgGrade}")
    print(f"Студентів в {faculty.Name}: {faculty.Count}")
    print(f"Хлопців в {faculty.Name}: {faculty.CountGender(Gender.XY)}")
    print(f"Дівчат в {faculty.Name}: {faculty.CountGender(Gender.XX)}")
