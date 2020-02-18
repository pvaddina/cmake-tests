cmake_minimum_required(VERSION 3.5.1)
project(Add-Library)

set (FOO_VALUE "This is a FOO cache variable" CACHE STRING "Some cache variable for demo purposes")

message("The value of FOO_VALUE=${FOO_VALUE})



set (SRCS src/add.cpp )

add_library(add STATIC ${SRCS})
target_include_directories(add 
PRIVATE
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/inc>
PUBLIC
  $<INSTALL_INTERFACE:${INSTALL_ROOT}/include>
)

