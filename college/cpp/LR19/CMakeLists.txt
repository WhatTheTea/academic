cmake_minimum_required(VERSION 3.5)

project(LR19 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(LR19 main.cpp
    Group.cpp Group.h main.cpp MainView.cpp MainView.h Null.h Student.cpp Student.h)

include(GNUInstallDirs)
install(TARGETS LR19
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)
