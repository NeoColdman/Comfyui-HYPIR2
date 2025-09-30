@echo off
REM HYPIR ComfyUI Plugin Installation Script for Windows
REM HYPIR ComfyUI 插件 Windows 安装脚本

echo ============================================================
echo HYPIR ComfyUI Plugin Installation
echo HYPIR ComfyUI 插件安装
echo ============================================================
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo 错误：Python 未安装或不在 PATH 中
    pause
    exit /b 1
)

echo Running installation script...
echo 运行安装脚本...
echo.

python install.py

if errorlevel 1 (
    echo.
    echo Installation failed. Please check the errors above.
    echo 安装失败。请检查上面的错误。
    pause
    exit /b 1
)

echo.
echo ============================================================
echo Installation completed!
echo 安装完成！
echo ============================================================
echo.
echo You can now restart ComfyUI to use the HYPIR plugin.
echo 现在可以重启 ComfyUI 来使用 HYPIR 插件了。
echo.

pause
