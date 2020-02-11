cmake_minimum_required(VERSION 3.5.1)
project(Calculator)

find_package(add REQUIRED)
find_package(mul REQUIRED)

add_executable(calculator calc.cpp)

target_link_libraries(calc 
PRIVATE
  calc::add
  calc::mul
)



