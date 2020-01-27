cmake_minimum_required(VERSION 3.5.1)
project(Calculator)

#message(${CMAKE_CURRENT_LIST_DIR})

add_executable(calc calc.cpp)
target_link_libraries(calc add mul)

install(TARGETS calc DESTINATION bin)

