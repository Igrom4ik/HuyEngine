# cmake/CPackReleaseConfig.cmake
# CPack configuration for creating a release ZIP containing only bin/, lib/ and README.md

# Package identity (can be overridden from command line via -D)
if (NOT DEFINED CPACK_PACKAGE_NAME)
    set(CPACK_PACKAGE_NAME "HuyEngine" CACHE STRING "CPack package name")
endif ()

if (NOT DEFINED CPACK_PACKAGE_VERSION)
    # Prefer HuyEngine_VERSION (set in top-level CMake), then PROJECT_VERSION, otherwise default to 1.0.0
    if (DEFINED HuyEngine_VERSION)
        set(CPACK_PACKAGE_VERSION "${HuyEngine_VERSION}" CACHE STRING "CPack package version")
    elseif (DEFINED PROJECT_VERSION)
        set(CPACK_PACKAGE_VERSION "${PROJECT_VERSION}" CACHE STRING "CPack package version")
    else ()
        set(CPACK_PACKAGE_VERSION "1.0.0" CACHE STRING "CPack package version")
    endif ()
endif ()

# Use ZIP and TGZ generator by default (can be overridden)
set(CPACK_GENERATOR "ZIP;TGZ" CACHE STRING "CPack generator")

# Ensure CMakeInstallPrefix exists — default to <binary>/install if not set
if (NOT DEFINED CMAKE_INSTALL_PREFIX)
    set(CMAKE_INSTALL_PREFIX "${CMAKE_BINARY_DIR}/install" CACHE PATH "Install prefix for packaging")
endif ()

# Output directory for produced archives (default: <build>/package)
set(CPACK_OUTPUT_FILE_PREFIX "${CMAKE_BINARY_DIR}/package" CACHE PATH "CPack output directory")

# Do not wrap contents into an extra top-level dir
set(CPACK_INCLUDE_TOPLEVEL_DIRECTORY OFF CACHE BOOL "Do not include top-level folder in archive")

# Only include bin/, lib/ and README.md from the install prefix
# Use pairs "<source>;<dest>" — avoid extra component field which can confuse CPack parsing
set(CPACK_INSTALLED_DIRECTORIES
        "${CMAKE_INSTALL_PREFIX}/bin;bin"
        "${CMAKE_INSTALL_PREFIX}/lib;lib"
        "${CMAKE_INSTALL_PREFIX}/README.md;."
)

# File name pattern: e.g. HuyEngine-1.2.3.zip
set(CPACK_PACKAGE_FILE_NAME "${CPACK_PACKAGE_NAME}-${CPACK_PACKAGE_VERSION}")

# Basic metadata (optional, but useful in archives)
set(CPACK_PACKAGE_VENDOR "HuyEngine Team" CACHE STRING "CPack package vendor")
set(CPACK_PACKAGE_DESCRIPTION_SUMMARY "HuyEngine release package" CACHE STRING "CPack description")

# Do not force component handling here (avoid adding ;ALL to entries)
# set(CPACK_COMPONENTS_ALL ALL)
