cmake_minimum_required(VERSION 3.5.1)
project(ArithmeticOperations-Library)

include(GenerateExportHeader)

set (HDR_SRCS arithmetic_op.h ${CMAKE_CURRENT_BINARY_DIR}/arithmeticop_exports.h)
set (CPP_SRCS src/arithmetic_op.cpp)

add_library(arithmeticop SHARED ${HDR_SRCS} ${CPP_SRCS})

target_include_directories(arithmeticop 
  PRIVATE
  ${CMAKE_CURRENT_BINARY_DIR}
  .)

target_include_directories(arithmeticop PRIVATE ../gen/addsub/inc ../gen/muldiv/inc)
target_link_directories(arithmeticop PRIVATE ../gen/addsub/lib ../gen/muldiv/lib)
target_link_libraries(arithmeticop PRIVATE addsub muldiv)

# Generate the export headers automatically. The header is generated
# in the build directory itself
GENERATE_EXPORT_HEADER(arithmeticop
    BASE_NAME arithmeticop
    EXPORT_MACRO_NAME ARITHMETICOP_EXPORTS
    EXPORT_FILE_NAME arithmeticop_exports.h
    STATIC_DEFINE SHARED_EXPORTS_BUILT_AS_STATIC)

install(TARGETS arithmeticop DESTINATION arithmeticop/lib)
install(TARGETS arithmeticop DESTINATION bin)
install(FILES ${HDR_SRCS} ${CMAKE_CURRENT_BINARY_DIR}/arithmeticop_exports.h 
  DESTINATION arithmeticop/inc)
