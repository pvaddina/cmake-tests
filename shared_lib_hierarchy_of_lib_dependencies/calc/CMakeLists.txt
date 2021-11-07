cmake_minimum_required(VERSION 3.5.1)
project(Calculator)

add_executable(calc calc.cpp)
target_include_directories(calc PRIVATE ../gen/arithmeticop/inc)
target_link_directories(calc PRIVATE ../gen/arithmeticop/lib)
target_link_libraries(calc PRIVATE arithmeticop)

install(TARGETS calc DESTINATION bin)


