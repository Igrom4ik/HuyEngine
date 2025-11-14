
# version
set(HuyEngine_VERSION_MAJOR ${PROJECT_VERSION_MAJOR})
set(HuyEngine_VERSION_MINOR ${PROJECT_VERSION_MINOR})
set(HuyEngine_VERSION_PATCH ${PROJECT_VERSION_PATCH})
set(HuyEngine_VERSION ${PROJECT_VERSION})
configure_file(EngineConfig.h.template ${CMAKE_CURRENT_BINARY_DIR}/EngineConfig.h)

set(ENGINE_SOURCES
        Source/Core/Engine.cpp
        Source/Core/Engine.hpp
        ${CMAKE_CURRENT_BINARY_DIR}/EngineConfig.h
)

add_library(${PROJECT_NAME}Lib STATIC ${ENGINE_SOURCES})
target_include_directories(${PROJECT_NAME}Lib PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/Source ${CMAKE_CURRENT_BINARY_DIR})

# folders
set_target_properties(${PROJECT_NAME}Lib PROPERTIES FOLDER Engine)

include(${CMAKE_SOURCE_DIR}/Automation/CMAKE/CMakeHelpers.cmake)
create_ide_folders(ENGINE_SOURCES)
