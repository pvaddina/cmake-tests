cmake_minimum_required(VERSION 3.5.1)
project(ctool)

set (INSTALL_ROOT ${PROJECT_NAME})

find_package(add_mul_lib REQUIRED)

set (SRCS inc/calc.h src/calc.cpp src/ctool.cpp)

add_executable(${PROJECT_NAME} ${SRCS})

target_include_directories(${PROJECT_NAME} 
PRIVATE
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/inc>
)

target_link_libraries(${PROJECT_NAME} 
PRIVATE
  calc::add_mul_lib
)

install(TARGETS ${PROJECT_NAME} 
        DESTINATION ${INSTALL_ROOT}/bin
        EXPORT ${PROJECT_NAME}Export)
