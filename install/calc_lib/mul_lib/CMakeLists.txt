cmake_minimum_required(VERSION 3.5.1)
project(Mul-Library)

set (SRCS src/mul.cpp)

add_library(mul STATIC ${SRCS})
target_include_directories(mul PUBLIC inc)

install(TARGETS mul DESTINATION gen/lib EXPORT mulExport)
install(FILES inc/mul.h DESTINATION gen/include)
install(EXPORT mulExport FILE mul.cmake NAMESPACE calc:: DESTINATION gen/cmake)
