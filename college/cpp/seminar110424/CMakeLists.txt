cmake_minimum_required(VERSION 3.5)

project(seminar110424 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(seminar110424 main.cpp)

include(GNUInstallDirs)
install(TARGETS seminar110424
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)
