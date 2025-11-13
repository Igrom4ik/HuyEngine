"""
HuyEngine - Interactive Build Menu
Интерактивное меню для управления сборкой
"""

import os
import sys

try:
    from .build_config import BuildConfig, IDE, BuildSystem, Configuration, Platform, ToolPaths
except ImportError:
    from build_config import BuildConfig, IDE, BuildSystem, Configuration, Platform, ToolPaths


class Colors:
    """ANSI цвета для терминала"""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def disable():
        """Отключает цвета (для Windows без поддержки ANSI)"""
        Colors.HEADER = ''
        Colors.OKBLUE = ''
        Colors.OKCYAN = ''
        Colors.OKGREEN = ''
        Colors.WARNING = ''
        Colors.FAIL = ''
        Colors.ENDC = ''
        Colors.BOLD = ''
        Colors.UNDERLINE = ''


# Включаем поддержку ANSI в Windows 10+
if sys.platform == "win32":
    try:
        import ctypes
        kernel32 = ctypes.windll.kernel32
        # Включаем ANSI escape sequences
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)  # type: ignore
    except Exception:
        Colors.disable()


class BuildMenu:
    """Интерактивное меню сборки"""

    def __init__(self):
        self.running = True
        ToolPaths.initialize_tools()

    def clear_screen(self):
        """Очищает экран"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_header(self):
        """Выводит заголовок"""
        print(f"{Colors.BOLD}{Colors.OKCYAN}{'='*70}{Colors.ENDC}")
        print(f"{Colors.BOLD}{Colors.OKCYAN}{'HuyEngine - Build Automation Menu':^70}{Colors.ENDC}")
        print(f"{Colors.BOLD}{Colors.OKCYAN}{'='*70}{Colors.ENDC}\n")

    def print_current_config(self):
        """Print current configuration"""
        print(f"{Colors.BOLD}Current configuration:{Colors.ENDC}")
        print(f"  IDE:           {Colors.OKGREEN}{BuildConfig.current_ide.value}{Colors.ENDC}")
        print(f"  Build System:  {Colors.OKGREEN}{BuildConfig.current_build_system.value}{Colors.ENDC}")
        print(f"  Configuration: {Colors.OKGREEN}{BuildConfig.current_configuration.value}{Colors.ENDC}")
        print(f"  Platform:      {Colors.OKGREEN}{BuildConfig.current_platform.value}{Colors.ENDC}")
        print(f"  Build Folder:  {Colors.OKGREEN}{BuildConfig.get_build_folder()}{Colors.ENDC}")
        print()

    def print_tools_status(self):
        """Print detected tools status"""
        print(f"{Colors.BOLD}Tools status:{Colors.ENDC}")

        cmake_status = f"{Colors.OKGREEN}✓ Найден{Colors.ENDC}" if BuildConfig.CMAKE_PATH else f"{Colors.FAIL}✗ Не найден{Colors.ENDC}"
        print(f"  CMake:  {cmake_status}")
        if BuildConfig.CMAKE_PATH:
            print(f"          {BuildConfig.CMAKE_PATH}")

        ninja_status = f"{Colors.OKGREEN}✓ Найден{Colors.ENDC}" if BuildConfig.NINJA_PATH else f"{Colors.FAIL}✗ Не найден{Colors.ENDC}"
        print(f"  Ninja:  {ninja_status}")
        if BuildConfig.NINJA_PATH:
            print(f"          {BuildConfig.NINJA_PATH}")

        vs_status = f"{Colors.OKGREEN}✓ Найден{Colors.ENDC}" if BuildConfig.VCVARSALL_PATH else f"{Colors.FAIL}✗ Не найден{Colors.ENDC}"
        print(f"  MSVC:   {vs_status}")
        if BuildConfig.CXX_COMPILER:
            print(f"          {BuildConfig.CXX_COMPILER}")
        print()

    def select_from_enum(self, enum_class, prompt):
        """Select value from enum"""
        print(f"\n{Colors.BOLD}{prompt}{Colors.ENDC}")
        options = list(enum_class)
        for i, option in enumerate(options, 1):
            print(f"  {i}. {option.value}")

        while True:
            try:
                choice = input(f"\n{Colors.OKCYAN}Select option (1-{len(options)}): {Colors.ENDC}").strip()
                if not choice:
                    return None
                idx = int(choice) - 1
                if 0 <= idx < len(options):
                    return options[idx]
                else:
                    print(f"{Colors.FAIL}Invalid choice. Try again.{Colors.ENDC}")
            except ValueError:
                print(f"{Colors.FAIL}Enter a number.{Colors.ENDC}")
            except KeyboardInterrupt:
                return None

    def menu_configure(self):
        """Configuration menu"""
        self.clear_screen()
        self.print_header()
        print(f"{Colors.BOLD}BUILD CONFIGURATION{Colors.ENDC}\n")

        # Select IDE
        ide = self.select_from_enum(IDE, "Select IDE:")
        if ide:
            BuildConfig.current_ide = ide

        # Select build system
        build_sys = self.select_from_enum(BuildSystem, "Select build system:")
        if build_sys:
            BuildConfig.current_build_system = build_sys

        # Select configuration
        config = self.select_from_enum(Configuration, "Select configuration:")
        if config:
            BuildConfig.current_configuration = config

        # Select platform
        platform = self.select_from_enum(Platform, "Select platform:")
        if platform:
            BuildConfig.current_platform = platform

        print(f"\n{Colors.OKGREEN}✓ Configuration updated!{Colors.ENDC}")
        input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")

    def menu_build_actions(self):
        """Build actions menu"""
        self.clear_screen()
        self.print_header()
        self.print_current_config()

        print(f"{Colors.BOLD}BUILD ACTIONS{Colors.ENDC}\n")
        print("  1. Generate (Project generation)")
        print("  2. Build (Build project)")
        print("  3. Rebuild (Rebuild project)")
        print("  4. Clean (Clean current folder)")
        print("  5. Clean All (Clean all build folders)")
        print("  6. Run (Run executable)")
        print("  0. Back")

        choice = input(f"\n{Colors.OKCYAN}Select action: {Colors.ENDC}").strip()

        if choice == "1":
            self.action_generate()
        elif choice == "2":
            self.action_build()
        elif choice == "3":
            self.action_rebuild()
        elif choice == "4":
            self.action_clean()
        elif choice == "5":
            self.action_clean_all()
        elif choice == "6":
            self.action_run()
        elif choice == "0":
            return
        else:
            print(f"{Colors.FAIL}Invalid choice.{Colors.ENDC}")
            input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")

    def action_generate(self):
        """Генерация проекта"""
        print(f"\n{Colors.OKBLUE}→ Запуск генерации проекта...{Colors.ENDC}\n")
        from build_actions import generate_project
        success = generate_project()

        if success:
            print(f"\n{Colors.OKGREEN}✓ Проект успешно сгенерирован!{Colors.ENDC}")
        else:
            print(f"\n{Colors.FAIL}✗ Ошибка генерации проекта.{Colors.ENDC}")

        input(f"\n{Colors.OKCYAN}Нажмите Enter для продолжения...{Colors.ENDC}")

    def action_build(self):
        """Сборка проекта"""
        print(f"\n{Colors.OKBLUE}→ Запуск сборки проекта...{Colors.ENDC}\n")
        from build_actions import build_project
        success = build_project()

        if success:
            print(f"\n{Colors.OKGREEN}✓ Проект успешно собран!{Colors.ENDC}")
        else:
            print(f"\n{Colors.FAIL}✗ Ошибка сборки проекта.{Colors.ENDC}")

        input(f"\n{Colors.OKCYAN}Нажмите Enter для продолжения...{Colors.ENDC}")

    def action_rebuild(self):
        """Пересборка проекта"""
        print(f"\n{Colors.OKBLUE}→ Запуск пересборки проекта...{Colors.ENDC}\n")
        from build_actions import rebuild_project
        success = rebuild_project()

        if success:
            print(f"\n{Colors.OKGREEN}✓ Проект успешно пересобран!{Colors.ENDC}")
        else:
            print(f"\n{Colors.FAIL}✗ Ошибка пересборки проекта.{Colors.ENDC}")

        input(f"\n{Colors.OKCYAN}Нажмите Enter для продолжения...{Colors.ENDC}")

    def action_clean(self):
        """Очистка текущей папки сборки"""
        print(f"\n{Colors.WARNING}→ Удаление папки {BuildConfig.get_build_folder()}...{Colors.ENDC}\n")
        from build_actions import clean_build_folder
        success = clean_build_folder(BuildConfig.get_build_folder())

        if success:
            print(f"\n{Colors.OKGREEN}✓ Build folder deleted!{Colors.ENDC}")
        else:
            print(f"\n{Colors.WARNING}⚠ Build folder does not exist or already deleted.{Colors.ENDC}")

        input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")

    def action_clean_all(self):
        """Очистка всех папок сборки"""
        print(f"\n{Colors.WARNING}→ Удаление всех папок сборки...{Colors.ENDC}\n")
        from build_actions import clean_all_build_folders
        clean_all_build_folders()

        print(f"\n{Colors.OKGREEN}✓ Все папки сборки удалены!{Colors.ENDC}")
        input(f"\n{Colors.OKCYAN}Нажмите Enter для продолжения...{Colors.ENDC}")

    def action_run(self):
        """Run application"""
        print(f"\n{Colors.OKBLUE}→ Running application...{Colors.ENDC}\n")
        from build_actions import run_executable
        run_executable()

        input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")

    def menu_tools(self):
        """Меню инструментов"""
        self.clear_screen()
        self.print_header()
        self.print_tools_status()

        print(f"{Colors.BOLD}ИНСТРУМЕНТЫ{Colors.ENDC}\n")
        print("  1. Clang-Format (Форматирование кода)")
        print("  2. Обновить пути к инструментам")
        print("  0. Назад")

        choice = input(f"\n{Colors.OKCYAN}Выберите действие: {Colors.ENDC}").strip()

        if choice == "1":
            self.tool_clang_format()
        elif choice == "2":
            ToolPaths.initialize_tools()
            print(f"\n{Colors.OKGREEN}✓ Paths updated!{Colors.ENDC}")
            input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")
        elif choice == "0":
            return
        else:
            print(f"{Colors.FAIL}Invalid choice.{Colors.ENDC}")
            input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")

    def tool_clang_format(self):
        """Run clang-format"""
        print(f"\n{Colors.OKBLUE}→ Running clang-format...{Colors.ENDC}\n")
        from build_actions import run_clang_format
        success = run_clang_format()

        if success:
            print(f"\n{Colors.OKGREEN}✓ Formatting completed!{Colors.ENDC}")
        else:
            print(f"\n{Colors.FAIL}✗ Formatting error.{Colors.ENDC}")

        input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")

    def main_menu(self):
        """Main menu"""
        while self.running:
            self.clear_screen()
            self.print_header()
            self.print_current_config()

            print(f"{Colors.BOLD}MAIN MENU{Colors.ENDC}\n")
            print("  1. Configuration")
            print("  2. Build")
            print("  3. Tools")
            print("  0. Exit")

            choice = input(f"\n{Colors.OKCYAN}Select menu item: {Colors.ENDC}").strip()

            if choice == "1":
                self.menu_configure()
            elif choice == "2":
                self.menu_build_actions()
            elif choice == "3":
                self.menu_tools()
            elif choice == "0":
                self.running = False
                print(f"\n{Colors.OKGREEN}Goodbye!{Colors.ENDC}\n")
            else:
                print(f"{Colors.FAIL}Invalid choice. Try again.{Colors.ENDC}")
                input(f"\n{Colors.OKCYAN}Press Enter to continue...{Colors.ENDC}")

    def run(self):
        """Run menu"""
        try:
            self.main_menu()
        except KeyboardInterrupt:
            print(f"\n\n{Colors.WARNING}Interrupted by user.{Colors.ENDC}")
            print(f"{Colors.OKGREEN}Goodbye!{Colors.ENDC}\n")


if __name__ == "__main__":
    menu = BuildMenu()
    menu.run()

