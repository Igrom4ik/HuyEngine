# CLion: запуск Build Menu по горячей клавише

Ниже — одна рабочая, простая и переносимая настройка. Откроется отдельное окно PowerShell 7 с интерактивным меню сборки.

## 1) External Tool

- Program: `C:\Windows\System32\cmd.exe`
- Arguments:

```
/c start "HuyEngine Build" pwsh.exe -NoExit -Command "Set-Location '$ProjectFileDir$'; python '.\Automation\build_menu.py'"
```

- Working directory: `$ProjectFileDir$`

## 2) Хоткей

- Settings → Keymap → External Tools → HuyEngine Build Menu
- ПКМ → Add Keyboard Shortcut → нажмите, например, `Ctrl+NumPad1`

## 3) Проверка

- Нажмите ваш хоткей в CLion — откроется новое окно PowerShell 7 с меню

## Требования

- PowerShell 7 (`pwsh.exe`) в PATH
- Python 3.x в PATH

## Если что-то пошло не так

- Ошибка CreateProcess 0x80070002: укажите полный путь к `cmd.exe` и используйте `Set-Location '$ProjectFileDir$'`
- `wt.exe` не запускается: используйте `cmd /c start` (как в инструкции выше), либо укажите полный путь к Windows
  Terminal

## Альтернатива (Windows Terminal)

Если установлен Windows Terminal, можно попробовать так:

- Program: `C:\Users\<USERNAME>\AppData\Local\Microsoft\WindowsApps\wt.exe`
- Arguments:

```
-w 0 new-tab --title "HuyEngine Build" pwsh.exe -NoExit -Command "Set-Location '$ProjectFileDir$'; python '.\Automation\build_menu.py'"
```

## Быстрые инструменты (опционально)

- Quick Build:

```
/c start "Build" pwsh.exe -NoExit -Command "Set-Location '$ProjectFileDir$'; python -c 'from Automation.build_actions import build_project; build_project()'"
```

- Quick Clean:

```
/c start "Clean" pwsh.exe -NoExit -Command "Set-Location '$ProjectFileDir$'; python -c 'from Automation.build_actions import clean_all_build_folders; clean_all_build_folders()'"
```

