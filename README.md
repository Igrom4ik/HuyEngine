# HuyEngine

[![Документация: GitHub Copilot](https://img.shields.io/badge/Документация-GitHub%20Copilot-blue?logo=github)](https://github.com/features/copilot)

Custom Game Engine built with C++ and CMake.

> 📝 **Документация и дизайн документации созданы благодаря GitHub Copilot**

## 🚀 Quick Start

### New Build System v2.0 (Recommended)

```bash
# Interactive menu (easiest way)
build.bat

# Or quick commands
build.bat rebuild    # Full rebuild
build.bat build      # Build
build.bat run        # Run
```

**📖 Full documentation:** [docs/README.md](docs/README.md) | [Automation/README.md](Automation/README.md)

### Features

- 🎮 **Interactive menu** - no need to remember commands
- 🛠️ **Multiple IDEs** - Visual Studio, CLion, VSCode support
- ⚡ **Fast builds** - Ninja, MSBuild, Unix Makefiles
- 📁 **Smart folders** - separate folders per configuration
- 🔍 **Auto-detection** - finds CMake, Ninja, Visual Studio automatically

## Build System

### Prerequisites

- CMake 3.15+
- Python 3.6+
- Visual Studio 2019/2022 (MSVC)
- Ninja (optional, recommended for speed)

**Quick install (Windows):**

```bash
choco install python cmake ninja
```

### Quick Start - New System

```bash
# Interactive menu
build.bat

# Command line
build.bat rebuild              # Full rebuild
build.bat build                # Build only
build.bat clean-all            # Clean all
build.bat run                  # Run app

# With options
build.bat -i clion -c debug generate
build.bat -b ninja -c release build
```

### Build Commands (New System v2.0)

| Command               | Description                   |
|-----------------------|-------------------------------|
| `build.bat`           | Interactive menu (easiest)    |
| `build.bat generate`  | Generate CMake project        |
| `build.bat build`     | Build project                 |
| `build.bat rebuild`   | Full rebuild                  |
| `build.bat clean`     | Clean current folder          |
| `build.bat clean-all` | Clean all build folders       |
| `build.bat run`       | Run executable                |
| `build.bat format`    | Format code with clang-format |

### Examples

```bash
# Interactive menu (recommended)
build.bat

# Quick commands
build.bat rebuild
build.bat run

# With options
build.bat -i clion -c debug generate
build.bat -b ninja -c release build
# Release build
build.bat rebuild --configuration Release
build.bat run --configuration Release
# Clean build directory
build.bat clean
# Format code
build.bat clang_format
```

## Project Structure

```
HuyEngine/
├── CMakeLists.txt          # Root CMake configuration
├── main.cpp                # Application entry point
├── build.bat               # Build automation wrapper
├── Engine/                 # Engine module
│   ├── CMakeLists.txt      # Engine CMake configuration
│   ├── Core/               # Public headers
│   └── Source/             # Implementation files
└── Automation/             # Build automation scripts
    ├── automation.py       # Python build script
    ├── build.bat           # Legacy wrapper
    └── CMAKE/              # CMake helper functions
        └── CmakeHelpers.cmake
```

## Configuration

Build settings can be modified in `Automation/automation.py`:

```python
class Config:
    CMAKE_PATH = r"C:\Program Files\CMake\bin\cmake.exe"
    NINJA_PATH = r"C:\ProgramData\chocolatey\bin\ninja.exe"
    CXX_COMPILER = r"C:\Program Files\...\cl.exe"
    CMAKE_GENERATOR = "Ninja"
    BUILD_FOLDER = "build"
    EXECUTABLE_NAME = "HuyEngine.exe"
```

## Development

### Adding New Source Files

1. Add `.cpp` files to `Engine/Source/`
2. Add `.h/.hpp` headers to `Engine/Core/`
3. CMake will automatically pick them up (using `file(GLOB_RECURSE)`)
4. Rebuild: `build.bat rebuild`

### IDE Support

- **CLion**: Open project root, CMake configuration is automatic
- **Visual Studio**: Generate VS solution: change `CMAKE_GENERATOR` to `"Visual Studio 17 2022"`

## 🤖 Документация

Дизайн документации и вся документация проекта созданы благодаря **GitHub Copilot**.

### Документы:

- [docs/BUILD_QUICKSTART.md](docs/BUILD_QUICKSTART.md) - быстрый старт сборки
- [docs/BUILD_INSTRUCTIONS_RU.md](docs/BUILD_INSTRUCTIONS_RU.md) - полная инструкция по сборке
- [docs/CLION_HOTKEYS.md](docs/CLION_HOTKEYS.md) - запуск Build Menu по хоткею в CLion
- [Automation/BUILD_SYSTEM_README.md](Automation/BUILD_SYSTEM_README.md) - документация системы автоматизации
- [Automation/BUILD_EXAMPLES.md](Automation/BUILD_EXAMPLES.md) - примеры использования
- [Automation/BUILD_FAQ.md](Automation/BUILD_FAQ.md) - часто задаваемые вопросы

---

## License

[Your License Here]

---

<center>
  <em>Документация и дизайн созданы с помощью <strong>GitHub Copilot</strong> 🤖</em>
</center>
