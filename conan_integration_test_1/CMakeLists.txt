cmake_minimum_required(VERSION 3.15)
project(ConanCMakeExample LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find Conan-generated package configuration
find_package(fmt CONFIG REQUIRED)

# Add executable
add_executable(example src/main.cpp)

# Link against fmt library
target_link_libraries(example PRIVATE fmt::fmt)
