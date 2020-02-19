project(All-about-Aliases)

set(CMAKE_CXX_STANDARD 11)

add_executable(alias alias.cpp)

# Add a test with a Name, and the command to execute
# The COMMAND keyword is followed by the executable name, and 
# all the arguments it needs to run
add_test(NAME Know-all-about-Aliases
      COMMAND alias)
