"""
HuyEngine - Build Configuration
Configuration for various IDEs and build systems
"""

from enum import Enum
from pathlib import Path
import os


class IDE(Enum):
    """Supported IDEs"""
    VISUAL_STUDIO = "Visual Studio"
    CLION = "CLion"
    VSCODE = "VSCode"
    MANUAL = "Manual (Command Line)"


class BuildSystem(Enum):
    """Supported build systems"""
    NINJA = "Ninja"
    MSBUILD = "MSBuild (Visual Studio)"
    MAKE = "Unix Makefiles"


class Configuration(Enum):
    """Build configurations"""
    DEBUG = "Debug"
    RELEASE = "Release"
    RELWITHDEBINFO = "RelWithDebInfo"
    MINSIZEREL = "MinSizeRel"


class Platform(Enum):
    """Platforms"""
    X64 = "x64"
    WIN32 = "Win32"
    ARM64 = "ARM64"


class BuildConfig:
    """Main build configuration"""

    # Project root directory
    PROJECT_ROOT = Path(__file__).parent.parent

    # Executable name
    EXECUTABLE_NAME = "HuyEngine.exe"

    # Source directories for clang-format
    SOURCE_DIRS = ["Engine", "main.cpp"]

    # Tool paths (will be automatically detected)
    CMAKE_PATH = None
    NINJA_PATH = None
    CXX_COMPILER = None
    C_COMPILER = None
    VCVARSALL_PATH = None

    # Current settings
    current_ide = IDE.MANUAL
    current_build_system = BuildSystem.NINJA
    current_configuration = Configuration.DEBUG
    current_platform = Platform.X64

    # Build options
    verbose = False
    clean_first = True

    @staticmethod
    def get_build_folder():
        """Returns the build folder depending on IDE and build system"""
        if BuildConfig.current_ide == IDE.CLION:
            if BuildConfig.current_configuration == Configuration.DEBUG:
                return "cmake-build-debug"
            elif BuildConfig.current_configuration == Configuration.RELEASE:
                return "cmake-build-release"
            else:
                return f"cmake-build-{BuildConfig.current_configuration.value.lower()}"
        elif BuildConfig.current_ide == IDE.VISUAL_STUDIO:
            return "vs-build"
        else:
            return "build"

    @staticmethod
    def get_cmake_generator():
        """Returns CMake generator depending on the build system"""
        if BuildConfig.current_build_system == BuildSystem.NINJA:
            return "Ninja"
        elif BuildConfig.current_build_system == BuildSystem.MSBUILD:
            # Detect Visual Studio version
            vs_versions = [
                ("Visual Studio 17 2022", r"C:\Program Files\Microsoft Visual Studio\2022"),
                ("Visual Studio 16 2019", r"C:\Program Files (x86)\Microsoft Visual Studio\2019"),
            ]
            for gen, path in vs_versions:
                if os.path.exists(path):
                    return gen
            return "Visual Studio 17 2022"  # Default
        elif BuildConfig.current_build_system == BuildSystem.MAKE:
            return "Unix Makefiles"
        return "Ninja"


class ToolPaths:
    """Development tool paths"""

    # Possible CMake paths
    CMAKE_PATHS = [
        r"C:\Program Files\CMake\bin\cmake.exe",
        r"C:\Program Files (x86)\CMake\bin\cmake.exe",
        r"cmake",  # From PATH
    ]

    # Possible Ninja paths
    NINJA_PATHS = [
        r"C:\ProgramData\chocolatey\bin\ninja.exe",
        r"C:\Program Files\Ninja\ninja.exe",
        r"ninja",  # From PATH
    ]

    # Possible Visual Studio paths
    VISUAL_STUDIO_PATHS = [
        # VS 2022
        (r"C:\Program Files\Microsoft Visual Studio\2022\Community", "2022"),
        (r"C:\Program Files\Microsoft Visual Studio\2022\Professional", "2022"),
        (r"C:\Program Files\Microsoft Visual Studio\2022\Enterprise", "2022"),
        # VS 2019
        (r"C:\Program Files (x86)\Microsoft Visual Studio\2019\Community", "2019"),
        (r"C:\Program Files (x86)\Microsoft Visual Studio\2019\Professional", "2019"),
        (r"C:\Program Files (x86)\Microsoft Visual Studio\2019\Enterprise", "2019"),
    ]

    @staticmethod
    def find_cmake():
        """Find CMake in the system"""
        import shutil
        for path in ToolPaths.CMAKE_PATHS:
            if path == "cmake":
                found = shutil.which("cmake")
                if found:
                    return found
            elif os.path.exists(path):
                return path
        return None

    @staticmethod
    def find_ninja():
        """Find Ninja in the system"""
        import shutil
        for path in ToolPaths.NINJA_PATHS:
            if path == "ninja":
                found = shutil.which("ninja")
                if found:
                    return found
            elif os.path.exists(path):
                return path
        return None

    @staticmethod
    def find_visual_studio():
        """Find Visual Studio in the system"""
        for vs_path, version in ToolPaths.VISUAL_STUDIO_PATHS:
            if os.path.exists(vs_path):
                # Find compilers
                vc_tools = Path(vs_path) / "VC" / "Tools" / "MSVC"
                if vc_tools.exists():
                    # Get the latest compiler version
                    versions = sorted([d for d in vc_tools.iterdir() if d.is_dir()], reverse=True)
                    if versions:
                        msvc_version = versions[0]
                        compiler_path = msvc_version / "bin" / "Hostx64" / "x64" / "cl.exe"
                        vcvarsall = Path(vs_path) / "VC" / "Auxiliary" / "Build" / "vcvarsall.bat"

                        if compiler_path.exists() and vcvarsall.exists():
                            return {
                                "version": version,
                                "path": vs_path,
                                "msvc_version": msvc_version.name,
                                "compiler": str(compiler_path),
                                "vcvarsall": str(vcvarsall)
                            }
        return None

    @staticmethod
    def initialize_tools():
        """Initialize tool paths"""
        # Find CMake
        BuildConfig.CMAKE_PATH = ToolPaths.find_cmake()
        if not BuildConfig.CMAKE_PATH:
            print("⚠ CMake not found in the system!")

        # Find Ninja
        BuildConfig.NINJA_PATH = ToolPaths.find_ninja()
        if not BuildConfig.NINJA_PATH:
            print("⚠ Ninja not found in the system!")

        # Find Visual Studio
        vs_info = ToolPaths.find_visual_studio()
        if vs_info:
            BuildConfig.CXX_COMPILER = vs_info["compiler"]
            BuildConfig.C_COMPILER = vs_info["compiler"]
            BuildConfig.VCVARSALL_PATH = vs_info["vcvarsall"]
        else:
            print("⚠ Visual Studio not found in the system!")

        # Load user configuration
        ToolPaths.load_user_config()

    @staticmethod
    def load_user_config():
        """Load user configuration if it exists"""
        try:
            import importlib.util
            user_config_path = Path(__file__).parent / "user_config.py"

            if user_config_path.exists():
                spec = importlib.util.spec_from_file_location("user_config", user_config_path)
                user_config = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(user_config)

                # Apply user settings
                if hasattr(user_config, 'apply_user_config'):
                    user_config.apply_user_config(BuildConfig)
                    print("✓ User configuration loaded")
        except Exception as e:
            print(f"⚠ Error loading user configuration: {e}")
