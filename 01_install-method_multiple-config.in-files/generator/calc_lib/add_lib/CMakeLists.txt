cmake_minimum_required(VERSION 3.5.1)
project(Add-Library)

set (SRCS src/add.cpp )

add_library(add STATIC ${SRCS})
target_include_directories(add 
PRIVATE
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/inc>
PUBLIC
  $<INSTALL_INTERFACE:${INSTALL_ROOT}/include>
)

install(TARGETS add 
        DESTINATION ${INSTALL_ROOT}/lib 
        EXPORT addExport)

install(DIRECTORY inc/ 
        DESTINATION ${INSTALL_ROOT}/include 
        FILES_MATCHING PATTERN "*.h")

install(EXPORT addExport 
        FILE add.cmake 
        NAMESPACE calc:: 
        DESTINATION ${INSTALL_ROOT}/cmake)

include(CMakePackageConfigHelpers)

# generate the config file that is includes the exports
configure_package_config_file(${CMAKE_CURRENT_SOURCE_DIR}/Config.cmake.in
                              "${CMAKE_CURRENT_BINARY_DIR}/addConfig.cmake"
                              INSTALL_DESTINATION "${INSTALL_ROOT}/cmake"
                              NO_SET_AND_CHECK_MACRO
                              NO_CHECK_REQUIRED_COMPONENTS_MACRO
                              )

write_basic_package_version_file(${CMAKE_CURRENT_BINARY_DIR}/addConfigVersion.cmake
                                  VERSION 1.1.10
                                  COMPATIBILITY SameMajorVersion
                                  )

install(FILES ${CMAKE_CURRENT_BINARY_DIR}/addConfigVersion.cmake ${CMAKE_CURRENT_BINARY_DIR}/addConfig.cmake 
        DESTINATION ${INSTALL_ROOT}/cmake
       )

export(EXPORT addExport
  FILE "${CMAKE_CURRENT_BINARY_DIR}/add.cmake"
)


