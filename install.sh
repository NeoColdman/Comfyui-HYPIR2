#!/bin/bash
# HYPIR ComfyUI Plugin Installation Script for Linux/Mac
# HYPIR ComfyUI 插件 Linux/Mac 安装脚本

echo "============================================================"
echo "HYPIR ComfyUI Plugin Installation"
echo "HYPIR ComfyUI 插件安装"
echo "============================================================"
echo ""

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    if ! command -v python &> /dev/null; then
        echo "Error: Python is not installed or not in PATH"
        echo "错误：Python 未安装或不在 PATH 中"
        exit 1
    fi
    PYTHON_CMD="python"
else
    PYTHON_CMD="python3"
fi

echo "Using Python: $PYTHON_CMD"
$PYTHON_CMD --version
echo ""

echo "Running installation script..."
echo "运行安装脚本..."
echo ""

$PYTHON_CMD install.py

if [ $? -ne 0 ]; then
    echo ""
    echo "Installation failed. Please check the errors above."
    echo "安装失败。请检查上面的错误。"
    exit 1
fi

echo ""
echo "============================================================"
echo "Installation completed!"
echo "安装完成！"
echo "============================================================"
echo ""
echo "You can now restart ComfyUI to use the HYPIR plugin."
echo "现在可以重启 ComfyUI 来使用 HYPIR 插件了。"
echo ""
