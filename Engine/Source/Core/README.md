# HuyEngine Core Modules

## Engine Module (`Engine.ixx`)

The main engine module that provides core functionality for the HuyEngine.

### Features

- **Singleton Pattern**: Single engine instance across the application
- **Configuration System**: Flexible engine configuration with `EngineConfig`
- **Game Loop**: High-performance game loop with delta time tracking
- **FPS Counter**: Built-in FPS monitoring and display
- **Frame Timing**: Target FPS limiting (configurable)

### Usage

```cpp
import Engine;

int main() {
    // Get engine instance
    auto& engine = HuyEngine::Engine::GetInstance();

    // Configure engine
    HuyEngine::EngineConfig config;
    config.applicationName = "My Game";
    config.windowWidth = 1920;
    config.windowHeight = 1080;
    config.targetFPS = 60;

    // Initialize
    if (!engine.Initialize(config)) {
        return -1;
    }

    // Run
    engine.Run();

    // Cleanup
    engine.Shutdown();

    return 0;
}
```

### API Reference

#### EngineConfig

Configuration structure for engine initialization.

**Members:**
- `std::string applicationName` - Application name (default: "HuyEngine Application")
- `unsigned int windowWidth` - Window width in pixels (default: 1280)
- `unsigned int windowHeight` - Window height in pixels (default: 720)
- `bool fullscreen` - Fullscreen mode (default: false)
- `bool vsync` - VSync enabled (default: true)
- `unsigned int targetFPS` - Target frames per second (default: 60)

#### Engine Class

Main engine class (Singleton).

**Methods:**
- `static Engine& GetInstance()` - Get the singleton instance
- `bool Initialize(const EngineConfig& config)` - Initialize the engine
- `void Run()` - Start the main game loop
- `void Shutdown()` - Shutdown the engine
- `[[nodiscard]] bool IsRunning() const` - Check if engine is running
- `[[nodiscard]] unsigned int GetFPS() const` - Get current FPS
- `[[nodiscard]] unsigned long long GetFrameNumber() const` - Get current frame number
- `void Stop()` - Stop the engine loop

### Module System

HuyEngine uses **C++20 modules** (`.ixx` files) for better compilation times and cleaner dependencies.

**Supported Extensions:**
- `.ixx` - C++20 module interface files
- `.cppm` - Alternative C++20 module extension (optional)

### Requirements

- **CMake 3.28+** (for C++20 module support)
- **C++20** compiler:
  - MSVC 19.30+ (Visual Studio 2022)
  - Clang 16+ (with `-std=c++20`)
  - GCC 11+ (with `-std=c++20`)

### Build Configuration

The project is configured to use C++20 modules in `CMakeLists.txt`:

```cmake
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_EXPERIMENTAL_CXX_MODULE_CMAKE_API "2182bf5c-ef0d-489a-91da-49dbc3090d2a")
set(CMAKE_EXPERIMENTAL_CXX_MODULE_DYNDEP ON)
```

### Future Modules

Planned modules for the engine:

- `Renderer` - Graphics rendering system
- `Input` - Input handling (keyboard, mouse, gamepad)
- `Audio` - Audio playback system
- `Physics` - Physics simulation
- `Scene` - Scene management
- `ECS` - Entity Component System
- `Assets` - Asset loading and management

## Module Guidelines

When creating new modules:

1. Use `.ixx` extension for module interface files
2. Start with `export module ModuleName;`
3. Use `export` keyword for public APIs
4. Keep internal implementation private (no `export`)
5. Use `[[nodiscard]]` for getter methods
6. Add comprehensive documentation with `/// @brief`
7. Follow the namespace convention: `HuyEngine::ModuleName`

### Example Module Structure

```cpp
// ModuleName.ixx
export module ModuleName;

import <iostream>;

namespace HuyEngine {
    /// @brief Module description
    export class ModuleName {
    public:
        void PublicMethod();
        
    private:
        void InternalMethod();
        int m_data;
    };
}
```

