# HuyEngine - Game Engine SDK v1.0.0

Modern C++ Game Engine for high-performance game development.

## 📦 Package Contents

```
bin/            - Demo application & runtime
lib/            - Engine library (binaries) for game projects
README.md       - Short instructions and license reference
```

### File Purpose

**Release Binary Package (what you get when downloading the runtime ZIP):**

- `bin/HuyEngineApp.exe` - Demo application showcasing engine capabilities
- `lib/` - Engine library files (.lib/.a/.dll as appropriate)
- `README.md` - Short instructions and license

> Important: the release binary package intentionally DOES NOT include source files (.cpp) or
> header files (.h/.hpp). Source code and headers belong to the Source Code/SDK distribution only.

### File Purpose (detailed)

**For End Users (Running Demo):**

- `bin/HuyEngineApp.exe` - Demo application that runs using the engine binaries
- ✅ **Runs with the provided binaries** - No need for headers or source files in the runtime package

**For Game Developers (Building YOUR game with HuyEngine):**

- Use the separate Source Code / SDK distribution which contains `include/` and full sources.
- The development package contains:
    - `include/HuyEngine/` - Public headers
    - `lib/` - Static/import libraries for linking

## 🚀 Quick Start

### Running the Demo (from release binary package)

```powershell
cd bin
.\HuyEngineApp.exe
```

The executable uses only binary libraries from `lib/` and does not require headers at runtime.

### Building Your Game with HuyEngine (requires SDK / source package)

```cmake
cmake_minimum_required(VERSION 3.20)
project(MyGame)

set(CMAKE_CXX_STANDARD 23)

# Point to HuyEngine SDK (contains include/ and lib/)
set(HUYENGINE_ROOT "/path/to/HuyEngine-SDK-1.0.0-Windows")
include_directories(${HUYENGINE_ROOT}/include)
link_directories(${HUYENGINE_ROOT}/lib)

add_executable(MyGame src/main.cpp)
target_link_libraries(MyGame HuyEngineLib)
```

### Example Game Code

```cpp
#include <HuyEngine/Core/Engine.hpp>
#include <iostream>

int main() {
    // Initialize the game engine
    HuyEngine::Engine engine;
    
    std::cout << "HuyEngine v" << engine.version() << std::endl;
    
    return 0;
}
```

## 🛠️ System Requirements

**Runtime (for playing games):**

- Windows 10+ or Linux (Ubuntu 20.04+)
- x64 architecture

**Development (for building games):**

- C++23 compatible compiler:
    - GCC 13+ / Clang 16+ / MSVC 2022+
- CMake 3.20+ (recommended)
- Ninja build system (optional)

## 📄 License

See LICENSE file in the repository.

---

**HuyEngine** - Built for performance, designed for creativity.
