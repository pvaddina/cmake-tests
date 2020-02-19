cmake_minimum_required(VERSION 3.5.1)
project(Add-Library)

set (NON_CACHE_VARIABLE "Default value of non-cache variable")
set (STRING_CACHE_VARIABLE "Default value of cache variable" CACHE STRING "Demo string cache variable")
set (BOOL_CACHE_VARIABLE OFF CACHE BOOL "Demo bool cache variable")

message("NON_CACHE_VARIABLE=${NON_CACHE_VARIABLE}")
message("STRING_CACHE_VARIABLE=${STRING_CACHE_VARIABLE}")
message("BOOL_CACHE_VARIABLE=${BOOL_CACHE_VARIABLE}")

set (SRCS src/add.cpp )

add_library(add STATIC ${SRCS})
target_include_directories(add 
PRIVATE
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/inc>
PUBLIC
  $<INSTALL_INTERFACE:${INSTALL_ROOT}/include>
)

