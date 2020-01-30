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

install(TARGETS mul DESTINATION gen/lib EXPORT mulExport)
install(FILES inc/mul.h DESTINATION gen/include)
install(EXPORT mulExport FILE mul.cmake NAMESPACE calc:: DESTINATION gen/cmake)
