cmake_minimum_required(VERSION 3.5.1)
project(Mul-Library)

set (SRCS src/mul.cpp)

add_library(mul STATIC ${SRCS})

# 
# Note if the directory is simply set as 'inc' instead of the generator expression, this 
# will generate a warning as a hard coded path valid only for this PC will be generated and 
# used in the export configurations, which will obviously not work when consumed on another PC
# 
# Also note that without adding the include directory with the INSTALL_INTERFACE, the directory
# where the project is installed cannot be accessed for include files
target_include_directories(mul
PRIVATE
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/inc>
PUBLIC
  $<INSTALL_INTERFACE:${INSTALL_ROOT}/include>
)

#############################################################################################
# Installing the library and the include headers
#############################################################################################

# Install target files of the project and define an export configuration called 'mulExport'.
# Note that the export file itself is not generated and installed in this command
install(TARGETS mul 
        EXPORT mulExport
        RUNTIME DESTINATION ${INSTALL_ROOT}
        LIBRARY DESTINATION ${INSTALL_ROOT}/lib
        ARCHIVE DESTINATION ${INSTALL_ROOT}/lib)

# Specify install rules to install the include files
install(DIRECTORY inc/ 
        DESTINATION ${INSTALL_ROOT}/include 
        FILES_MATCHING PATTERN "*.h")

# Install the export configuration as 'mul.cmake' with the given namespae and at the given destination
install(EXPORT mulExport
        FILE mul.cmake 
        NAMESPACE calc:: 
        DESTINATION ${INSTALL_ROOT}/cmake)

#############################################################################################
# Steps to generate the mulConfig.cmake which is required for find_package to discover the lib
#############################################################################################
include(CMakePackageConfigHelpers)

# generate the config file that includes the exports
configure_package_config_file(${CMAKE_CURRENT_SOURCE_DIR}/Config.cmake.in
                              "${CMAKE_CURRENT_BINARY_DIR}/mulConfig.cmake"
                              INSTALL_DESTINATION "${INSTALL_ROOT}/cmake"
                              NO_SET_AND_CHECK_MACRO
                              NO_CHECK_REQUIRED_COMPONENTS_MACRO
                             )

# generate the version file for the config file
write_basic_package_version_file(${CMAKE_CURRENT_BINARY_DIR}/mulConfigVersion.cmake
                                  VERSION 1.1.10
                                  COMPATIBILITY SameMajorVersion
                                  )
# Install the generated configuration files
install(FILES ${CMAKE_CURRENT_BINARY_DIR}/mulConfigVersion.cmake ${CMAKE_CURRENT_BINARY_DIR}/mulConfig.cmake 
        DESTINATION ${INSTALL_ROOT}/cmake
        )

# At this point, we have generated a relocatable CMake Configuration for our project that 
# can be used after the project has been installed or packaged. If we want our project to 
# also be used from a build directory we only have to add the following to the bottom of the 
#top level CMakeLists.txt
export(EXPORT mulExport
  FILE "${CMAKE_CURRENT_BINARY_DIR}/mul.cmake"
)


