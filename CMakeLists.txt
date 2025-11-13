# File: `CMakeLists.txt` (root)
# Allow overriding minimal CMake version via -DCMAKE_MINIMUM_REQUIRED
if (DEFINED CMAKE_MINIMUM_REQUIRED)
    cmake_minimum_required(VERSION ${CMAKE_MINIMUM_REQUIRED})
else ()
    cmake_minimum_required(VERSION 4.2.0)
endif ()

# Project name can be overridden via -DPROJECT_NAME
if (NOT DEFINED PROJECT_NAME)
    set(PROJECT_NAME "HuyEngine")
endif ()

# Project definition
project(${PROJECT_NAME} VERSION 0.1 LANGUAGES CXX)

# C++ standard (can be overridden via -DPROJECT_CXX_STANDARD)
if (DEFINED PROJECT_CXX_STANDARD)
    set(CMAKE_CXX_STANDARD ${PROJECT_CXX_STANDARD})
else ()
    set(CMAKE_CXX_STANDARD 20)
endif ()
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Enable C++20 modules
set(CMAKE_EXPERIMENTAL_CXX_MODULE_CMAKE_API "2182bf5c-ef0d-489a-91da-49dbc3090d2a")
set(CMAKE_EXPERIMENTAL_CXX_MODULE_DYNDEP ON)

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
add_executable(${PROJECT_NAME}
        main.cpp
)

# Ensure CMake knows the C++ standard requirement for targets that use C++ modules
# CMake requires an explicit target_compile_features (cxx_std_20 or newer)
# when FILE_SET CXX_MODULES is used.
if (DEFINED CMAKE_CXX_COMPILER_ID AND NOT CMAKE_CXX_COMPILER_ID STREQUAL "")
    message(STATUS "Detected CXX compiler: ${CMAKE_CXX_COMPILER_ID} ${CMAKE_CXX_COMPILER_VERSION}")
    # prefer feature corresponding to requested standard
    if (CMAKE_CXX_STANDARD GREATER_EQUAL 23)
        target_compile_features(${PROJECT_NAME} PUBLIC cxx_std_23)
    elseif (CMAKE_CXX_STANDARD GREATER_EQUAL 20)
        target_compile_features(${PROJECT_NAME} PUBLIC cxx_std_20)
    elseif (CMAKE_CXX_STANDARD GREATER_EQUAL 17)
        target_compile_features(${PROJECT_NAME} PUBLIC cxx_std_17)
    endif ()
else ()
    message(WARNING "C++ compiler not identified yet; skipping target_compile_features and relying on CMAKE_CXX_STANDARD=${CMAKE_CXX_STANDARD}.")
endif ()

# Add module sources
target_sources(${PROJECT_NAME}
        PUBLIC
        FILE_SET CXX_MODULES FILES
        Engine/Source/Core/Engine.ixx
)

# Link libraries if needed
# target_link_libraries(${PROJECT_NAME} PRIVATE EngineLib)

set_property(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} PROPERTY VS_STARTUP_PROJECT ${PROJECT_NAME})

include(${CMAKE_SOURCE_DIR}/Automation/CMAKE/CmakeHelpers.cmake)
system_info()
