cmake_minimum_required(VERSION 3.5.1)
project(AddSub-Library)

include(GenerateExportHeader)

set (HDR_SRCS add.h sub.h ${CMAKE_CURRENT_BINARY_DIR}/addsub_exports.h)
set (CPP_SRCS src/add.cpp src/sub.cpp)

add_library(addsub SHARED ${HDR_SRCS} ${CPP_SRCS})

target_include_directories(addsub 
  PRIVATE
  ${CMAKE_CURRENT_BINARY_DIR}
  .)

# Generate the export headers automatically. The header is generated
# in the build directory itself
GENERATE_EXPORT_HEADER(addsub
    BASE_NAME addsub
    EXPORT_MACRO_NAME ADDSUB_EXPORTS
    EXPORT_FILE_NAME addsub_exports.h
    STATIC_DEFINE SHARED_EXPORTS_BUILT_AS_STATIC)

install(TARGETS addsub DESTINATION addsub/lib)
install(TARGETS addsub DESTINATION bin)
install(FILES ${HDR_SRCS} ${CMAKE_CURRENT_BINARY_DIR}/addsub_exports.h 
  DESTINATION addsub/inc)
