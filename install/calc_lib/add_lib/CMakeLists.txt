cmake_minimum_required(VERSION 3.5.1)
project(Add-Library)

set (SRCS src/add.cpp )

add_library(add STATIC ${SRCS})
target_include_directories(add PUBLIC $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/inc>)

install(TARGETS add 
        DESTINATION gen/lib 
        EXPORT addExport)

install(DIRECTORY inc/ 
        DESTINATION gen/include 
        FILES_MATCHING PATTERN "*.h")

install(EXPORT addExport 
        FILE add.cmake 
        NAMESPACE calc:: 
        DESTINATION gen/cmake)

