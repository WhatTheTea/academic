cmake_minimum_required(VERSION 3.5)

project(LR18 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(LR18 main.cpp
    sourcefiles.h sourcefiles.cpp

)

include(GNUInstallDirs)
install(TARGETS LR18
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)
