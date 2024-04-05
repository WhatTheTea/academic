cmake_minimum_required(VERSION 3.5)

project(LR20 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(LR20 main.cpp
  book.h book.cpp
  range.h range.cpp
  library.h library.cpp
  librarycli.h librarycli.cpp)

include(GNUInstallDirs)
install(TARGETS LR20
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)
