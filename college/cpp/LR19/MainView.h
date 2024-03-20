#ifndef MAINVIEW_H
#define MAINVIEW_H

#include "Group.h"

enum Menu {
    PrintAllMeanDesc = 1,
    PrintAllMeanAsc = 2,
	AddStudent = 3, 
	RemoveStudent = 4 };

struct studentConsoleView {
  Group group;

  studentConsoleView() { group = Group(); }
  void AddStudent();
  void RemoveStudent();
  void PrintAllMeanAscending();
  void PrintAllMeanDescending();
  void mainloop();
};
#endif // !MAINVIEW_H
