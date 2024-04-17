cmake_minimum_required(VERSION 3.5)

project(ekzamen LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(ekzamen Silchenko_first.cpp
  Silchenko_third.cpp
  Herhalo_first.cpp
  Herhalo_third.cpp

)

include(GNUInstallDirs)
install(TARGETS ekzamen
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)
