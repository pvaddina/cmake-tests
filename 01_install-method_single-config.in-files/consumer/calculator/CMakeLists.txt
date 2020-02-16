cmake_minimum_required(VERSION 3.5.1)
project(CalculatorTool)

find_package(add REQUIRED)
find_package(mul REQUIRED)

add_executable(ctool ctool.cpp)

target_link_libraries(ctool
PRIVATE
  calc::add
  calc::mul
)

install(TARGETS ctool
        DESTINATION calculator)



