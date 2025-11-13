# File: `CMakeLists.txt` (root)
cmake_minimum_required(VERSION 4.2.0)

# Project definition
project(HuyEngine VERSION 0.1 LANGUAGES C CXX)

# Options
option(BUILD_TESTS "Build tests" ON)

# Set output directories
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

set_property(GLOBAL PROPERTY USE_FOLDERS ON)
set(CMAKE_SUPPRESS_REGENERATION TRUE)

# Project structure
add_subdirectory(Engine)

# Main executable
add_executable(${PROJECT_NAME} main.cpp)

set_property(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} PROPERTY VS_STARTUP_PROJECT ${PROJECT_NAME})

include(${CMAKE_SOURCE_DIR}/Automation/CMAKE/CmakeHelpers.cmake)
system_info()
