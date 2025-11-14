# general info
cmake_minimum_required(VERSION 3.31.6)

# cpp options
set(CMAKE_CXX_STANDARD 23)

# common options
project(HuyEngine VERSION 1.0.0 LANGUAGES CXX)


set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

set_property(GLOBAL PROPERTY USE_FOLDERS ON)
set(CMAKE_SUPPRESS_REGENERATION TRUE)

# project structure
add_subdirectory(Engine)
add_subdirectory(App)

set_property(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} PROPERTY VS_STARTUP_PROJECT HuyEngineApp)

# Подключаем дополнительные CMake-хелперы только если файл существует
set(_helpers_path "${CMAKE_SOURCE_DIR}/Automation/CMAKE/CMakeHelpers.cmake")
if (EXISTS "${_helpers_path}")
    include("${_helpers_path}")
    if (COMMAND system_info)
        system_info()
    endif ()
else ()
    message(WARNING "Optional CMake helpers not found: ${_helpers_path}. Continuing without it.")
endif ()

# --- CPack (packaging) ---
install(TARGETS HuyEngineApp RUNTIME DESTINATION bin)
# Install package documentation
install(FILES ${CMAKE_SOURCE_DIR}/PACKAGE_README.md DESTINATION . RENAME README.md)

# Load release-specific CPack defaults (create cmake/CPackReleaseConfig.cmake)
if (EXISTS "${CMAKE_SOURCE_DIR}/cmake/CPackReleaseConfig.cmake")
    include("${CMAKE_SOURCE_DIR}/cmake/CPackReleaseConfig.cmake")
endif ()

# Ensure CPack module is loaded (this generates package targets such as 'package')
include(CPack)

# Helper target: build, install into CMAKE_INSTALL_PREFIX and then run packaging target
add_custom_target(package-release
        COMMAND ${CMAKE_COMMAND} --build "${CMAKE_BINARY_DIR}" --config Release --target install
        COMMAND ${CMAKE_COMMAND} --build "${CMAKE_BINARY_DIR}" --config Release --target package
        WORKING_DIRECTORY "${CMAKE_BINARY_DIR}"
        COMMENT "Build Release, install to ${CMAKE_INSTALL_PREFIX} and create release ZIP via CPack"
)
