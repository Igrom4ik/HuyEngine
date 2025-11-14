# common options
set(APP_TARGET HuyEngineApp)

# version
set(HuyEngine_VERSION_MAJOR ${PROJECT_VERSION_MAJOR})
set(HuyEngine_VERSION_MINOR ${PROJECT_VERSION_MINOR})
set(HuyEngine_VERSION_PATCH ${PROJECT_VERSION_PATCH})
set(HuyEngine_VERSION ${PROJECT_VERSION})
configure_file(EngineConfig.h.template ${CMAKE_CURRENT_BINARY_DIR}/EngineConfig.h)

set(APP_SOURCES
        Source/main.cpp
        Source/pch.cpp
        Source/pch.hpp
        ${CMAKE_CURRENT_BINARY_DIR}/EngineConfig.h
)

add_executable(${APP_TARGET} ${APP_SOURCES})
target_link_libraries(${APP_TARGET} PRIVATE ${PROJECT_NAME}Lib)
target_include_directories(${APP_TARGET} PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/Source ${CMAKE_CURRENT_BINARY_DIR})

# folders
set_target_properties(${APP_TARGET} PROPERTIES FOLDER App)

include(${CMAKE_SOURCE_DIR}/Automation/CMAKE/CmakeHelpers.cmake)
create_ide_folders(APP_SOURCES)
setup_precompiled_headers(${APP_TARGET} Source/pch.cpp Source/pch.hpp "${APP_SOURCES}")
