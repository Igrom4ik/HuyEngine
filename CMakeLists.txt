# general info
cmake_minimum_required(VERSION 3.31.6)

# cpp options
set(CMAKE_CXX_STANDARD 23)

# common options
project(HuyEngine VERSION 1.0.0 LANGUAGES CXX)

# Initialize HuyEngine version variables early so they can be overridden via -D
# Allow override from the cache (e.g. -DHuyEngine_VERSION:STRING=2.3.4)
if (NOT DEFINED HuyEngine_VERSION)
    set(HuyEngine_VERSION ${PROJECT_VERSION} CACHE STRING "HuyEngine version")
endif ()
if (NOT DEFINED HuyEngine_VERSION_MAJOR)
    set(HuyEngine_VERSION_MAJOR ${PROJECT_VERSION_MAJOR} CACHE STRING "HuyEngine version major")
endif ()
if (NOT DEFINED HuyEngine_VERSION_MINOR)
    set(HuyEngine_VERSION_MINOR ${PROJECT_VERSION_MINOR} CACHE STRING "HuyEngine version minor")
endif ()
if (NOT DEFINED HuyEngine_VERSION_PATCH)
    set(HuyEngine_VERSION_PATCH ${PROJECT_VERSION_PATCH} CACHE STRING "HuyEngine version patch")
endif ()

# Generate version.txt in build directory for scripts/CI to read (early)
if (EXISTS "${CMAKE_SOURCE_DIR}/cmake/version.txt.in")
    configure_file(${CMAKE_SOURCE_DIR}/cmake/version.txt.in ${CMAKE_BINARY_DIR}/version.txt @ONLY)
endif ()

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
# Install package documentation: prefer PACKAGE_README.md (renamed to README.md), fallback to README.md
if (EXISTS "${CMAKE_SOURCE_DIR}/PACKAGE_README.md")
    install(FILES "${CMAKE_SOURCE_DIR}/PACKAGE_README.md" DESTINATION . RENAME README.md)
elseif (EXISTS "${CMAKE_SOURCE_DIR}/README.md")
    install(FILES "${CMAKE_SOURCE_DIR}/README.md" DESTINATION .)
else ()
    message(WARNING "No PACKAGE_README.md or README.md found — package will not contain README")
endif ()

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

# Helper target to print current configured version
add_custom_target(print-version
        COMMAND ${CMAKE_COMMAND} -E echo "HuyEngine version: ${PROJECT_VERSION}"
        COMMENT "Print configured HuyEngine version"
)

# Shortcut to run package-release from command line: 'cmake --build . --target package-release'
add_custom_target(package-release-help
        COMMAND ${CMAKE_COMMAND} -E echo "Run: cmake --build <build-dir> --target package-release --config Release"
        COMMENT "Show how to run package-release target"
)
