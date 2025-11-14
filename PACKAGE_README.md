# HuyEngine - Game Engine SDK v1.0.0

Modern C++ Game Engine for high-performance game development.

## 📦 Package Contents

```
bin/            - Demo application & runtime
lib/            - Engine static library for game projects
include/        - Public Engine API headers
```

### File Purpose

**For End Users (Running Demo):**

- `bin/HuyEngineApp.exe` - Demo application showcasing engine capabilities
- ✅ **Runs standalone** - No additional files needed

**For Game Developers (Building Games):**

- `lib/libHuyEngineLib.a` - Engine library to link against
- `include/HuyEngine/` - Engine API headers for development

## 🚀 Quick Start

### Running the Demo

```bash
cd bin
./HuyEngineApp.exe
```

The executable is **statically linked** and runs independently.

### Building Your Game with HuyEngine

#### Option 1: CMake (Recommended)

```cmake
cmake_minimum_required(VERSION 3.20)
project(MyGame)

set(CMAKE_CXX_STANDARD 23)

# Point to HuyEngine SDK
set(HUYENGINE_ROOT "/path/to/HuyEngine-1.0.0-Windows")
include_directories(${HUYENGINE_ROOT}/include)
link_directories(${HUYENGINE_ROOT}/lib)

add_executable(MyGame src/main.cpp)
target_link_libraries(MyGame HuyEngineLib)
```

#### Option 2: Manual Compilation

```bash
# Compile your game
g++ -std=c++23 my_game.cpp \
    -I/path/to/HuyEngine/include \
    -L/path/to/HuyEngine/lib \
    -lHuyEngineLib \
    -o MyGame.exe
```

### Example Game Code

```cpp
#include <HuyEngine/Core/Engine.hpp>
#include <iostream>

int main() {
    // Initialize the game engine
    HuyEngine::Engine engine;
    
    std::cout << "HuyEngine v" << engine.version() << std::endl;
    
    // Your game loop here
    // engine.run();
    
    return 0;
}
```

## 🎮 Usage Scenarios

### Scenario 1: Just Want to See the Demo

✅ **Only need**: `bin/HuyEngineApp.exe`  
📁 Can delete: `lib/` and `include/` folders

### Scenario 2: Developing a Game

✅ **Need everything**:

- `lib/` - to link your game against the engine
- `include/` - to access engine API in your code
- `bin/` - optional (demo/reference)

## 🛠️ System Requirements

**Runtime (for playing games):**

- Windows 10+ or Linux (Ubuntu 20.04+)
- x64 architecture

**Development (for building games):**

- C++23 compatible compiler:
    - GCC 13+ / Clang 16+ / MSVC 2022+
- CMake 3.20+ (recommended)
- Ninja build system (optional)

## 📚 Engine Features

- Modern C++23 architecture
- Cross-platform (Windows/Linux)
- Lightweight core
- Extensible module system

## 🔗 Resources

- **GitHub Repository**: https://github.com/Igrom4ik/HuyEngine
- **Documentation**: https://github.com/Igrom4ik/HuyEngine/wiki
- **Issues & Support**: https://github.com/Igrom4ik/HuyEngine/issues

## 📄 License

See LICENSE file in the repository.

---

**HuyEngine** - Built for performance, designed for creativity.

