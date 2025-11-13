# VSCode Setup for HuyEngine

## ✅ Всё настроено!

### Конфигурация

- ✅ CMake интеграция
- ✅ MinGW/GCC компилятор
- ✅ Tasks для сборки
- ✅ Debug конфигурация
- ✅ Поддержка C++20

### Как собрать проект в VSCode

**Способ 1: Через Command Palette (Ctrl+Shift+P)**

1. `CMake: Configure` - настроить проект
2. `CMake: Build` - собрать проект
3. `F5` - запустить с отладкой

**Способ 2: Через меню Terminal → Run Task**

1. `CMake: Configure` - первая настройка
2. `CMake: Build` - сборка (Ctrl+Shift+B)
3. `Run HuyEngine` - запуск приложения

**Способ 3: Через наш Python скрипт**

1. Terminal → Run Task → `Build Menu (Python)`
2. Выберите нужное действие в меню

### Сборка из командной строки

**MinGW:**

```powershell
python Automation/automation_new.py generate --toolchain mingw --config debug
cmake --build build-mingw
```

**MSVC:**

```powershell
python Automation/automation_new.py generate --ide vs --build-system msbuild
cmake --build vs-build --config Debug
```

### Отладка в VSCode

1. Поставьте breakpoint (F9)
2. Нажмите F5
3. Приложение запустится в отладчике GDB

### Расширения VSCode (рекомендуется)

- ✅ C/C++ (Microsoft) - уже используется
- ✅ CMake Tools (Microsoft) - уже настроено
- 📦 CMake (twxs) - подсветка синтаксиса

### Troubleshooting

**VSCode не видит CMake**

- Установите CMake Tools: Ctrl+Shift+X → "CMake Tools"
- Перезапустите VSCode

### Горячие клавиши

- `Ctrl+Shift+B` - Build
- `F5` - Run with Debug
- `Ctrl+F5` - Run without Debug
- `Ctrl+Shift+P` - Command Palette
- `Ctrl+` ` - Terminal

