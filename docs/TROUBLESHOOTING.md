# Troubleshooting — частые проблемы

## Хоткей не срабатывает в CLion

- Проверьте, что хоткей назначен: Settings → Keymap → External Tools → HuyEngine Build Menu
- Включите Num Lock (для NumPad)
- Уберите конфликтующие привязки
- Перезапустите IDE (File → Invalidate Caches / Restart)
- Полная инструкция: [CLION_HOTKEYS.md](CLION_HOTKEYS.md)

## CreateProcess error=2 / 0x80070002

Система не находит файл при запуске External Tool.

- Используйте Program: `C:\Windows\System32\cmd.exe`
- В Arguments обязательно задайте каталог проекта: `Set-Location '$ProjectFileDir$'`
- Пример: см. [CLION_HOTKEYS.md](CLION_HOTKEYS.md)

## Windows Terminal (wt.exe) не запускается

- Укажите полный путь к `wt.exe` либо используйте `cmd /c start ... pwsh.exe`
- Альтернатива: запускайте напрямую `pwsh.exe -NoExit -Command "..."`

## Проблемы с Unicode/кодировкой

- См. итоговую инструкцию: [UNICODE_FIX_README.md](UNICODE_FIX_README.md)
- Краткая версия: [QUICK_UNICODE_FIX.md](QUICK_UNICODE_FIX.md)

## clang-cl / компиляторы

- Быстрый фикс: [Automation/QUICK_FIX_CLANG_CL.md](../Automation/QUICK_FIX_CLANG_CL.md)

## Остались вопросы?

- Посмотрите [FAQ](../Automation/BUILD_FAQ.md) или [Примеры](../Automation/BUILD_EXAMPLES.md)

