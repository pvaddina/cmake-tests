cmake_minimum_required(VERSION 3.5.1)
project(Mul-Library)

set (SRCS src/mul.cpp)

add_library(mul STATIC ${SRCS})
# 
# Note if the directory is simply set as 'inc' instead of the generator expression, this will generate a warning
# as a hard coded path valid only for this PC will be generated and used in the export configurations, which
# will obviously not work when consumed on another PC
# 
target_include_directories(mul PUBLIC $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/inc>)

# Install target files of the project and define an export called 'mulTarget'.
# Note that the export file itself is not generated and installed in this command
install(TARGETS mul 
        EXPORT mulTarget
        RUNTIME DESTINATION gen
        LIBRARY DESTINATION gen/lib
        ARCHIVE DESTINATION gen/lib)

# Specify install rules to install the include files
install(DIRECTORY inc/ 
        DESTINATION gen/include 
        FILES_MATCHING PATTERN "*.h")

install(EXPORT mulTarget
        FILE mulTarget.cmake 
        NAMESPACE calc:: 
        DESTINATION gen/cmake)


