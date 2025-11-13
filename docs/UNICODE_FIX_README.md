# Unicode Encoding Fix - v2.0.1

## Проблема

При запуске системы сборки в Windows консоли с кодировкой cp1251 возникала ошибка:

```
UnicodeEncodeError: 'charmap' codec can't encode character '\u2713' in position 7: character maps to <undefined>
```

Это происходило при использовании Unicode символов (✓, ✗, ⚠, →) в выводе программы.

## Решение

Добавлена автоматическая настройка UTF-8 кодировки для `sys.stdout` и `sys.stderr` во всех модулях Python:

```python
import sys
import io

# Fix Unicode output for Windows console
if sys.platform == "win32":
    try:
        # Set UTF-8 encoding for stdout and stderr
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
    except Exception:
        pass
```

## Изменённые файлы

1. `Automation/automation_new.py` - главный скрипт
2. `Automation/build_menu.py` - интерактивное меню
3. `Automation/build_actions.py` - действия сборки
4. `Automation/build_config.py` - конфигурация
5. `BUILD_INSTRUCTIONS_RU.md` - документация (добавлен раздел устранения неполадок)
6. `CHANGELOG.md` - история изменений

## Тестирование

Для проверки работы Unicode символов используйте:

```powershell
python test_unicode.py
```

Если вы видите символы ✓, ✗, ⚠, → (а не вопросительные знаки), то исправление работает!

## Альтернативные решения

Если проблема всё ещё возникает, можно:

1. **Установить кодировку UTF-8 в PowerShell:**
   ```powershell
   [Console]::OutputEncoding = [System.Text.Encoding]::UTF8
   ```

2. **Установить переменную окружения:**
   ```powershell
   $env:PYTHONIOENCODING="utf-8"
   ```

3. **Добавить в профиль PowerShell (`$PROFILE`):**
   ```powershell
   [Console]::OutputEncoding = [System.Text.Encoding]::UTF8
   $env:PYTHONIOENCODING="utf-8"
   ```

## Дата исправления

**13 января 2025** - версия 2.0.1

