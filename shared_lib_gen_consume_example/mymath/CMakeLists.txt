cmake_minimum_required(VERSION 3.5.1)
project(MyMath-Library)

include(GenerateExportHeader)

set(HDR_INSTALL_PATH ${CMAKE_CURRENT_SOURCE_DIR}/inc)
set(LIB_INSTALL_PATH ${CMAKE_CURRENT_SOURCE_DIR}/lib)
set (HDR_SRCS add.h mul.h)
set (CPP_SRCS src/add.cpp src/mul.cpp)

add_library(mymath SHARED ${HDR_SRCS} ${CPP_SRCS})

target_include_directories(mymath 
PUBLIC
  .)

# Generate the export headers automatically. The header is generated
# in the build directory itself
GENERATE_EXPORT_HEADER(mymath
    BASE_NAME mymath
    EXPORT_MACRO_NAME MYMATH_EXPORTS
    EXPORT_FILE_NAME mymath_exports.h
    STATIC_DEFINE SHARED_EXPORTS_BUILT_AS_STATIC)

install(TARGETS mymath DESTINATION ${LIB_INSTALL_PATH})
install(FILES ${HDR_SRCS} ${CMAKE_CURRENT_BINARY_DIR}/mymath_exports.h 
  DESTINATION ${HDR_INSTALL_PATH})
