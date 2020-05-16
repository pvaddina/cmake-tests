cmake_minimum_required(VERSION 3.5.1)
project(Calculator)

add_executable(calc calc.cpp)
target_include_directories(calc PRIVATE ../gen/mymath/inc)
target_link_directories(calc PRIVATE ../gen/mymath/lib)
target_link_libraries(calc PRIVATE mymath)

install(TARGETS calc
  DESTINATION calc)


