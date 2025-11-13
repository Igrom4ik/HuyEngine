# Быстрое решение проблемы Unicode

Если вы столкнулись с ошибкой:

```
UnicodeEncodeError: 'charmap' codec can't encode character '\u2713'
```

## ✅ Решение уже применено!

Исправление автоматически включено в версии 2.0.1. Просто запустите скрипт снова:

```powershell
.\build.bat
```

или

```powershell
python Automation\automation_new.py
```

## Если проблема осталась

Выполните в PowerShell перед запуском:

```powershell
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
.\build.bat
```

## Автоматическое применение

Добавьте в ваш профиль PowerShell (`notepad $PROFILE`):

```powershell
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$env:PYTHONIOENCODING = "utf-8"
```

Затем перезапустите PowerShell.

## Проверка

Запустите тест:

```powershell
python test_unicode.py
```

Вы должны увидеть символы ✓, ✗, ⚠, →

---

**Версия исправления:** 2.0.1  
**Дата:** 13 января 2025

