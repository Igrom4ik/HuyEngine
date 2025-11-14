# HuyEngine - Архитектура проекта

> **Актуализировано**: 14.11.2025

## 🏗️ Обзор архитектуры

HuyEngine построен по модульной архитектуре с разделением на библиотеку движка и исполняемое приложение.

```
┌─────────────────────────────────────┐
│       HuyEngineApp.exe              │
│    (Исполняемый файл)               │
│                                     │
│  ┌───────────────────────────┐     │
│  │      main.cpp             │     │
│  │  - Точка входа            │     │
│  │  - Создание Engine        │     │
│  └───────────┬───────────────┘     │
│              │ использует          │
│              ▼                      │
│  ┌───────────────────────────┐     │
│  │   HuyEngineLib (static)   │     │
│  │  - Ядро движка            │     │
│  │  - Engine класс           │     │
│  │  - Базовый функционал     │     │
│  └───────────────────────────┘     │
└─────────────────────────────────────┘
```

## 📦 Модули

### 1. Engine (HuyEngineLib)

**Тип**: Статическая библиотека  
**Цель**: Ядро игрового движка  
**Расположение**: `Engine/Source/Core/`

#### Структура

```
Engine/
├── CMakeLists.txt              # Конфигурация сборки библиотеки
├── EngineConfig.h.template     # Шаблон для генерации версии
└── Source/
    └── Core/
        ├── Engine.hpp          # Публичный интерфейс класса Engine
        └── Engine.cpp          # Реализация Engine
```

#### Класс Engine

```cpp
namespace HuyEngine {
    class Engine final {
    public:
        Engine();  // Инициализация движка
        static constexpr std::string_view version(); // Версия
        ~Engine() = default;
    };
}
```

**Текущая функциональность:**

- Вывод приветственного сообщения с версией
- Версионирование через `EngineConfig.h`

**Планируемая функциональность:**

- Игровой цикл (game loop)
- Система логирования
- Управление временем (delta time)
- Менеджер систем
- ECS (Entity Component System)

#### CMake конфигурация

```cmake
add_library(HuyEngineLib STATIC ${ENGINE_SOURCES})
target_include_directories(HuyEngineLib PUBLIC
        ${CMAKE_CURRENT_SOURCE_DIR}/Source
        ${CMAKE_CURRENT_BINARY_DIR}
)
```

### 2. App (HuyEngineApp)

**Тип**: Исполняемый файл  
**Цель**: Точка входа приложения  
**Расположение**: `App/Source/`

#### Структура

```
App/
├── CMakeLists.txt              # Конфигурация сборки приложения
├── EngineConfig.h.template     # Шаблон для генерации версии
└── Source/
    ├── main.cpp                # Точка входа программы
    ├── pch.hpp                 # Precompiled header (заголовок)
    ├── pch.cpp                 # Precompiled header (реализация)
    └── Version.h               # Заголовок версии (пока пустой)
```

#### main.cpp

```cpp
#include "Core/Engine.hpp"
#include <cstdlib>

int main() {
    const HuyEngine::Engine engine;
    return EXIT_SUCCESS;
}
```

**Текущая функциональность:**

- Создание экземпляра движка
- Выход из программы

**Планируемая функциональность:**

- Инициализация окна
- Игровой цикл
- Обработка событий
- Загрузка игровых ресурсов

#### CMake конфигурация

```cmake
add_executable(HuyEngineApp ${APP_SOURCES})
target_link_libraries(HuyEngineApp PRIVATE HuyEngineLib)
target_include_directories(HuyEngineApp PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/Source
        ${CMAKE_CURRENT_BINARY_DIR}
)
```

**Особенности:**

- Поддержка PCH (Precompiled Headers) для MSVC
- Линкуется с `HuyEngineLib`
- Установлен как startup project в Visual Studio

## 🔧 CMake система

### Корневой CMakeLists.txt

```cmake
cmake_minimum_required(VERSION 3.31.6)
project(HuyEngine VERSION 1.0.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 23)

# Директории вывода
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

# Организация в папки
set_property(GLOBAL PROPERTY USE_FOLDERS ON)
set(CMAKE_SUPPRESS_REGENERATION TRUE)

# Подключение модулей
add_subdirectory(Engine)
add_subdirectory(App)

# Startup project для Visual Studio
set_property(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
        PROPERTY VS_STARTUP_PROJECT HuyEngineApp)
```

### CMakeHelpers.cmake

Вспомогательные функции для CMake:

#### system_info()

Выводит информацию о системе сборки:

- Операционная система (Windows/Linux)
- Компилятор (MSVC, Clang, GCC)
- Версии компилятора
- Флаги компиляции

#### setup_precompiled_headers()

Настраивает PCH для MSVC:

- Устанавливает `/Yc` для создания PCH
- Устанавливает `/Yu` для использования PCH
- Принудительное включение через `/FI`

#### create_ide_folders()

Создает иерархию папок в IDE:

- Группирует файлы по их расположению
- Создает папки в Solution Explorer (Visual Studio)
- Упрощает навигацию в проекте

#### setup_conan()

Настраивает интеграцию с Conan:

- Загружает conan_provider.cmake
- Настраивает профили хоста и сборки
- Для будущей интеграции зависимостей

### Версионирование

Система автоматической генерации версий:

**Шаблон** (`EngineConfig.h.template`):

```cpp
#pragma once

#define Engine_VERSION_MAJOR @HuyEngine_VERSION_MAJOR@
#define Engine_VERSION_MINOR @HuyEngine_VERSION_MINOR@
#define Engine_VERSION_PATCH @HuyEngine_VERSION_PATCH@
#define Engine_VERSION_STRING "@HuyEngine_VERSION@"
```

**Генерация** (в CMakeLists.txt):

```cmake
set(HuyEngine_VERSION_MAJOR ${PROJECT_VERSION_MAJOR})
set(HuyEngine_VERSION_MINOR ${PROJECT_VERSION_MINOR})
set(HuyEngine_VERSION_PATCH ${PROJECT_VERSION_PATCH})
set(HuyEngine_VERSION ${PROJECT_VERSION})

configure_file(
        EngineConfig.h.template
        ${CMAKE_CURRENT_BINARY_DIR}/EngineConfig.h
)
```

**Результат** (`EngineConfig.h`):

```cpp
#define Engine_VERSION_MAJOR 1
#define Engine_VERSION_MINOR 0
#define Engine_VERSION_PATCH 0
#define Engine_VERSION_STRING "1.0.0"
```

## 📁 Директории сборки

```
HuyEngine/
├── cmake-build-debug/           # CLion Debug (Ninja)
│   ├── bin/
│   │   ├── HuyEngineApp.exe     # Исполняемый файл
│   │   ├── HuyEngineLib.lib     # Статическая библиотека
│   │   └── *.pdb                # Debug symbols
│   ├── App/
│   │   └── EngineConfig.h       # Сгенерированный заголовок
│   └── Engine/
│       └── EngineConfig.h       # Сгенерированный заголовок
│
├── cmake-build-release/         # CLion Release (Ninja)
│   └── [аналогично debug]
│
└── cmake-build-debug-visual-studio/  # Visual Studio Debug (MSBuild)
    └── [аналогично debug]
```

## 🔄 Поток компиляции

```
1. CMake Configuration
   ├─> Обнаружение компилятора
   ├─> Установка C++23
   ├─> Генерация EngineConfig.h из шаблонов
   └─> Создание build файлов (Ninja/MSBuild)

2. Engine Library Build
   ├─> Компиляция Engine.cpp
   ├─> Создание HuyEngineLib.lib
   └─> Копирование в ${CMAKE_BINARY_DIR}/bin/

3. App Executable Build
   ├─> Компиляция pch.cpp (PCH)
   ├─> Компиляция main.cpp (с PCH)
   ├─> Линковка с HuyEngineLib
   └─> Создание HuyEngineApp.exe в ${CMAKE_BINARY_DIR}/bin/

4. Run
   └─> Запуск HuyEngineApp.exe
       └─> Вывод: "Hellow, I'm HuyEngine v1.0.0"
```

## 🎯 Паттерны и принципы

### Текущие

1. **Модульность**: Разделение на библиотеку и приложение
2. **Версионирование**: Единая точка управления версией (корневой CMakeLists.txt)
3. **Инкапсуляция**: Класс Engine с приватными деталями реализации
4. **RAII**: Использование конструктора/деструктора для управления ресурсами

### Планируемые

1. **ECS (Entity Component System)**: Для игровой логики
2. **Singleton**: Для систем (LogManager, ResourceManager)
3. **Factory Pattern**: Для создания игровых объектов
4. **Observer Pattern**: Для системы событий
5. **Strategy Pattern**: Для различных рендереров/платформ

## 🚀 Планируемое расширение архитектуры

```
HuyEngine (будущее)
├── Engine/
│   ├── Core/
│   │   ├── Engine          ✅ Текущее
│   │   ├── GameLoop        🔄 Планируется
│   │   ├── Time            🔄 Планируется
│   │   └── Logger          🔄 Планируется
│   ├── Rendering/          🔄 Планируется
│   │   ├── Renderer
│   │   ├── Camera
│   │   └── Mesh
│   ├── ECS/                🔄 Планируется
│   │   ├── Entity
│   │   ├── Component
│   │   └── System
│   ├── Physics/            🔄 Планируется
│   ├── Input/              🔄 Планируется
│   └── Resources/          🔄 Планируется
└── App/
    ├── Game                🔄 Планируется
    └── main                ✅ Текущее
```

## 📚 Связанная документация

- [PROJECT_STATUS.md](PROJECT_STATUS.md) — Текущий статус проекта
- [BUILD_QUICKSTART.md](BUILD_QUICKSTART.md) — Быстрый старт сборки
- [README.md](../README.md) — Основной README

---

<div align="center">
  <em>📝 Документация создана с помощью <strong>GitHub Copilot</strong> 🤖</em>
</div>

