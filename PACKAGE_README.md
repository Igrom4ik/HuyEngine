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
- ✅ **Runs standalone** - The exe already contains all engine code inside (statically linked)
- ❌ **Does NOT need** `lib/` or `include/` folders to run

**For Game Developers (Building YOUR game with HuyEngine):**

- `lib/libHuyEngineLib.a` - Engine library to link your game against
- `include/HuyEngine/` - Engine API headers to use in your game code
- ❌ **Does NOT need** `bin/` folder (that's just a demo)

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

### Scenario 1: Just Want to Run the Demo

**You are an END USER (player):**

✅ **Only need**: `bin/HuyEngineApp.exe`  
❌ **Can delete**: `lib/` and `include/` folders (not used at runtime)

```bash
# Just run it:
cd bin
./HuyEngineApp.exe
# That's it! The exe contains everything inside.
```

### Scenario 2: Developing Your Own Game

**You are a GAME DEVELOPER:**

✅ **Only need**: `lib/` + `include/`  
❌ **Can delete**: `bin/` folder (just a demo, not needed for development)

**Why you need headers:**

- Your game's `.cpp` files `#include <HuyEngine/Core/Engine.hpp>` to use the API
- Compiler needs headers to understand engine functions
- Linker needs `lib/libHuyEngineLib.a` to include engine code in YOUR game

**What happens:**

```
Your code (.cpp) + Headers (.hpp) → Compiler → Your game (.obj)
Your game (.obj) + Library (.a) → Linker → YourGame.exe
```

Your final `YourGame.exe` will also be **standalone** (statically linked), just like our demo.

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

