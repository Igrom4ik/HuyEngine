# Настройка горячих клавиш для Build Menu в JetBrains CLion

> ℹ️ Эта страница сохранена для подробностей, но упрощённая и актуальная инструкция находится
> здесь: [CLION_HOTKEYS.md](CLION_HOTKEYS.md)

## Кратко (современный способ)

- Используйте External Tool с Program: `C:\Windows\System32\cmd.exe` и Arguments:

```
/c start "HuyEngine Build" pwsh.exe -NoExit -Command "Set-Location '$ProjectFileDir$'; python '.\Automation\build_menu.py'"
```

- Назначьте хоткей в Keymap (например, Ctrl+NumPad1)

---

## Проблема

Горячие клавиши не работают для запуска `build_menu.bat` и других bat-файлов сборки.

## Решение

### Автоматическая настройка

Файл конфигурации External Tools уже создан:

- `.idea/tools/Build Menu.xml`

CLion автоматически загрузит эту конфигурацию при следующем запуске или перезагрузке проекта.

### Настройка горячих клавиш

1. **Откройте настройки**:
    - `File` → `Settings` (или `Ctrl+Alt+S`)

2. **Перейдите в Keymap**:
    - `Keymap` → `External Tools` → `Build Menu`

3. **Назначьте горячие клавиши** (рекомендуемые):
    - **Build Menu**: `Ctrl+Shift+B` (или `Alt+M`)
    - **Build (Quick)**: `Ctrl+F9` (или используйте стандартную)
    - **Generate (Quick)**: `Ctrl+Shift+G`
    - **Clean (Quick)**: `Ctrl+Shift+C`

### Как назначить горячую клавишу:

1. В окне Keymap найдите `External Tools` → `Build Menu`
2. Щелкните правой кнопкой мыши на нужный инструмент
3. Выберите `Add Keyboard Shortcut`
4. Нажмите желаемую комбинацию клавиш
5. Нажмите `OK`

### Проверка работы

После настройки вы сможете:

- Нажать `Ctrl+Shift+B` (или вашу горячую клавишу) → откроется Build Menu
- Использовать быстрые команды для генерации, сборки и очистки

## Доступные инструменты

После импорта конфигурации будут доступны:

1. **Build Menu** - Интерактивное меню сборки
    - Запускает `Automation\build_menu.bat`
    - Показывает полное меню с настройками

2. **Build (Quick)** - Быстрая сборка
    - Запускает `Automation\build.bat build`
    - Собирает проект с текущими настройками

3. **Generate (Quick)** - Быстрая генерация
    - Запускает `Automation\build.bat generate`
    - Генерирует проект с текущими настройками

4. **Clean (Quick)** - Быстрая очистка
    - Запускает `Automation\build.bat clean`
    - Очищает текущую папку сборки

## Альтернативный способ: Ручная настройка

Если автоматическая настройка не сработала:

1. **Откройте Settings**: `File` → `Settings` → `Tools` → `External Tools`
2. **Нажмите `+`** (Add)
3. **Заполните поля**:
    - **Name**: `Build Menu`
    - **Description**: `Launch HuyEngine Build Menu`
    - **Program**: `$ProjectFileDir$\Automation\build_menu.bat`
    - **Working directory**: `$ProjectFileDir$`
    - **Checkboxes**:
        - ✓ Synchronize files after execution
        - ✓ Open console for tool output

4. **Повторите** для остальных инструментов (Build, Generate, Clean)

## Использование из командной строки

Если горячие клавиши все еще не работают, можно использовать:

```batch
# Из корня проекта
.\Automation\build_menu.bat

# Или для быстрой сборки
.\Automation\build.bat build
```

## Использование из Run Configuration

Также можно создать Run Configuration:

1. `Run` → `Edit Configurations...`
2. Нажмите `+` → `Shell Script`
3. **Name**: `Build Menu`
4. **Script path**: `C:\DEVOPS\HuyEngine\Automation\build_menu.bat`
5. **Working directory**: `C:\DEVOPS\HuyEngine`

Теперь можно запускать через toolbar или `Shift+F10`.

## Проверка Python

Убедитесь, что Python доступен в PATH:

```powershell
python --version
# или
py --version
```

Если Python не найден, установите его или добавьте в PATH.

## Troubleshooting

### Проблема: "Python not found"

**Решение**: Установите Python 3.x и добавьте в PATH

### Проблема: Горячая клавиша не реагирует

**Решение**:

1. Перезагрузите проект (`File` → `Invalidate Caches / Restart`)
2. Проверьте, что в Keymap назначена горячая клавиша
3. Убедитесь, что горячая клавиша не конфликтует с другими

### Проблема: Консоль не открывается

**Решение**: В настройках External Tool включите "Open console for tool output"

## Дополнительная информация

- Документация по автоматизации: `Automation/README.md`
- Примеры использования: `Automation/BUILD_EXAMPLES.md`
- Инструкции по сборке: `docs/BUILD_QUICKSTART.md`
