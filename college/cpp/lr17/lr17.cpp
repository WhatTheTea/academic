#include "MainView.h"

int main(int argc, const char **argv) {
  auto studentsView = studentConsoleView();
  studentsView.mainloop();
  return 0;
}
