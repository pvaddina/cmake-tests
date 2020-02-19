cmake_minimum_required(VERSION 3.5.1)

project(Demo-ctest-with-examples)

# First enable testing
# Make sure this is before any subdirectory is added
enable_testing()

add_subdirectory(all_about_aliases)
add_subdirectory(all_about_constexpr)
