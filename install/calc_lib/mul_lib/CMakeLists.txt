cmake_minimum_required(VERSION 3.5.1)
project(Mul-Library)

set (SRCS src/mul.cpp)

add_library(mul STATIC ${SRCS})
# 
# Note if the directory is simply set as 'inc' instead of the generator expression, this will generate a warning
# as a hard coded path valid only for this PC will be generated and used in the export configurations, which
# will obviously not work when consumed on another PC
# 
target_include_directories(mul PUBLIC $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/inc>)

# Install target files of the project and define an export called 'mulTarget'.
# Note that the export file itself is not generated and installed in this command
install(TARGETS mul 
        EXPORT mulTarget
        RUNTIME DESTINATION calc_lib
        LIBRARY DESTINATION calc_lib/lib
        ARCHIVE DESTINATION calc_lib/lib)

# Specify install rules to install the include files
install(DIRECTORY inc/ 
        DESTINATION calc_lib/include 
        FILES_MATCHING PATTERN "*.h")


install(EXPORT mulTarget
        FILE mul.cmake 
        NAMESPACE calc:: 
        DESTINATION calc_lib/cmake)

include(CMakePackageConfigHelpers)

# generate the config file that is includes the exports
configure_package_config_file(${CMAKE_CURRENT_SOURCE_DIR}/Config.cmake.in
                              "${CMAKE_CURRENT_BINARY_DIR}/mulConfig.cmake"
                              INSTALL_DESTINATION "calc_lib/cmake"
                              NO_SET_AND_CHECK_MACRO
                              NO_CHECK_REQUIRED_COMPONENTS_MACRO
                              )

write_basic_package_version_file(${CMAKE_CURRENT_BINARY_DIR}/mulConfigVersion.cmake
                                  VERSION 1.1.10
                                  COMPATIBILITY SameMajorVersion
                                  )

install(FILES ${CMAKE_CURRENT_BINARY_DIR}/mulConfigVersion.cmake ${CMAKE_CURRENT_BINARY_DIR}/mulConfig.cmake 
        DESTINATION calc_lib/cmake
        )


