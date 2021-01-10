cmake_minimum_required(VERSION 3.5.1)
project(cshared)

set (INSTALL_ROOT ${PROJECT_NAME})

find_package(add_lib REQUIRED)
find_package(mul_lib REQUIRED)

set (SRCS inc/calc.h src/calc.cpp src/ctool.cpp $<TARGET_OBJECTS:calc::add_lib> $<TARGET_OBJECTS:calc::mul_lib>)

add_library(${PROJECT_NAME} SHARED ${SRCS})
target_include_directories(${PROJECT_NAME} 
PRIVATE
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/inc>
PUBLIC
  $<INSTALL_INTERFACE:${INSTALL_ROOT}/include>
)

target_link_libraries(${PROJECT_NAME} 
PRIVATE
  calc::add_lib
  calc::mul_lib
)

install(TARGETS ${PROJECT_NAME} 
        DESTINATION ${INSTALL_ROOT}/lib 
        EXPORT ${PROJECT_NAME}Export)

install(DIRECTORY inc/ 
        DESTINATION ${INSTALL_ROOT}/include 
        FILES_MATCHING PATTERN "*.h")

install(EXPORT ${PROJECT_NAME}Export 
        FILE ${PROJECT_NAME}.cmake 
        NAMESPACE calc:: 
        DESTINATION ${INSTALL_ROOT}/cmake)

include(CMakePackageConfigHelpers)

# generate the config file that is includes the exports
configure_package_config_file(${CMAKE_CURRENT_SOURCE_DIR}/Config.cmake.in
                              "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}Config.cmake"
                              INSTALL_DESTINATION "${INSTALL_ROOT}/cmake"
                              NO_SET_AND_CHECK_MACRO
                              NO_CHECK_REQUIRED_COMPONENTS_MACRO
                              )

write_basic_package_version_file(${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}ConfigVersion.cmake
                                  VERSION 1.1.10
                                  COMPATIBILITY SameMajorVersion
                                  )

install(FILES ${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}ConfigVersion.cmake ${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}Config.cmake 
        DESTINATION ${INSTALL_ROOT}/cmake
       )

export(EXPORT ${PROJECT_NAME}Export
  FILE "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}.cmake"
)


