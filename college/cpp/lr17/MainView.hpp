#ifndef MAINVIEW_H
#define MAINVIEW_H

#include "Group.h"

enum Menu { 
	SameMean = 1, 
	PrintEveryone = 2, 
	AddStudent = 3, 
	RemoveStudent = 4 };

struct studentConsoleView {
  Group group;

  studentConsoleView() { group = Group(); }
  void AddStudent();
  void RemoveStudent();
  void PrintAll();
  void SearchSameSecondMean();
  void mainloop();
};
#endif // !MAINVIEW_H