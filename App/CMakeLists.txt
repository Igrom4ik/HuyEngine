# App subproject (executable)

set(APP_TARGET HuyEngineApp)

# Version header generation
configure_file(EngineConfig.h.template ${CMAKE_CURRENT_SOURCE_DIR}/Source/EngineConfig.h)

set(APP_SOURCES
        Source/main.cpp
        Source/pch.cpp
        Source/pch.hpp
        Source/EngineConfig.h
)

add_executable(${APP_TARGET} ${APP_SOURCES})

# Link with the engine library defined in ../Engine/CMakeLists.txt
target_link_libraries(${APP_TARGET} PRIVATE HuyEngineLib)

target_include_directories(${APP_TARGET} PRIVATE ${CMAKE_SOURCE_DIR}/Engine/Source ${CMAKE_CURRENT_SOURCE_DIR}/Source)

# IDE folders and grouping (like Engine)
set_property(TARGET ${APP_TARGET} PROPERTY FOLDER App)
source_group(TREE ${CMAKE_CURRENT_SOURCE_DIR}/Source PREFIX "Source" FILES ${APP_SOURCES})

include(${CMAKE_SOURCE_DIR}/Automation/CMAKE/CMakeHelpers.cmake)
create_ide_folders(APP_SOURCES)
setup_precompiled_headers(${APP_TARGET} Source/pch.cpp Source/pch.hpp "${APP_SOURCES}")
