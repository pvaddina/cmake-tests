cmake_minimum_required(VERSION 3.5.1)
project(MulDiv-Library)

include(GenerateExportHeader)

set (HDR_SRCS div.h mul.h ${CMAKE_CURRENT_BINARY_DIR}/muldiv_exports.h)
set (CPP_SRCS src/div.cpp src/mul.cpp)

add_library(muldiv SHARED ${HDR_SRCS} ${CPP_SRCS})

target_include_directories(muldiv 
  PRIVATE
  ${CMAKE_CURRENT_BINARY_DIR}
  .)

# Generate the export headers automatically. The header is generated
# in the build directory itself
GENERATE_EXPORT_HEADER(muldiv
    BASE_NAME muldiv
    EXPORT_MACRO_NAME MULDIV_EXPORTS
    EXPORT_FILE_NAME muldiv_exports.h
    STATIC_DEFINE SHARED_EXPORTS_BUILT_AS_STATIC)

install(TARGETS muldiv DESTINATION muldiv/lib)
install(TARGETS muldiv DESTINATION bin)
install(FILES ${HDR_SRCS} ${CMAKE_CURRENT_BINARY_DIR}/muldiv_exports.h 
  DESTINATION muldiv/inc)
