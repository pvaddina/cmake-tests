cmake_minimum_required(VERSION 3.5.1)
project(Add-Library)

set (SRCS src/add.cpp )

add_library(add STATIC ${SRCS})
target_include_directories(add PUBLIC inc)


