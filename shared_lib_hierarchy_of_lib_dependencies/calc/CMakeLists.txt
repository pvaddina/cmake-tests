cmake_minimum_required(VERSION 3.5.1)
project(Calculator)

add_executable(calc calc.cpp)

target_include_directories(calc PRIVATE ../gen/arithmeticop/inc)
#
# Do not manually link to all dependencies ... 
#target_link_directories(calc PRIVATE ../gen/arithmeticop/lib ../gen/addsub/lib ../gen/muldiv/lib)
# 
# Instead force the linker not to check for dependencies during Linking (they are still needed at runtime)
# 
target_link_directories(calc PRIVATE ../gen/arithmeticop/lib)
if (UNIX)
  set (CMAKE_EXE_LINKER_FLAGS "-Wl,--unresolved-symbols=ignore-in-shared-libs")
endif()
#target_link_options(calc PRIVATE "LINKER:-Wl,--unresolved-symbols=ignore-in-shared-libs")

target_link_libraries(calc PRIVATE arithmeticop)

install(TARGETS calc DESTINATION bin)


