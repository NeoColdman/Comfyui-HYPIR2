#!/usr/bin/env python3
"""
HYPIR ComfyUI Plugin Installation Script
HYPIR ComfyUI 插件安装脚本

This script helps install all dependencies including FlashAttention 2.
本脚本帮助安装所有依赖，包括 FlashAttention 2。
"""

import sys
import subprocess
import platform
import os

def check_cuda():
    """Check if CUDA is available and get version"""
    try:
        import torch
        if torch.cuda.is_available():
            cuda_version = torch.version.cuda
            device_name = torch.cuda.get_device_name(0)
            compute_cap = torch.cuda.get_device_capability(0)
            print(f"✓ CUDA detected: {cuda_version}")
            print(f"✓ GPU: {device_name}")
            print(f"✓ Compute Capability: {compute_cap[0]}.{compute_cap[1]}")
            
            if compute_cap >= (7, 5):
                print("✓ GPU is compatible with FlashAttention 2")
                return True, cuda_version
            else:
                print("✗ GPU compute capability < 7.5, FlashAttention not supported")
                return False, cuda_version
        else:
            print("✗ CUDA not available")
            return False, None
    except ImportError:
        print("! PyTorch not found, cannot check CUDA")
        return None, None

def install_dependencies(skip_flash_attention=False):
    """Install dependencies from requirements.txt"""
    print("\n" + "="*60)
    print("Installing dependencies...")
    print("安装依赖...")
    print("="*60 + "\n")
    
    # Read requirements.txt
    requirements_path = os.path.join(os.path.dirname(__file__), "requirements.txt")
    if not os.path.exists(requirements_path):
        print(f"✗ requirements.txt not found at {requirements_path}")
        return False
    
    with open(requirements_path, 'r') as f:
        requirements = f.readlines()
    
    # Filter out FlashAttention if requested
    if skip_flash_attention:
        print("⚠ Skipping FlashAttention installation")
        requirements = [req for req in requirements if 'flash-attn' not in req.lower()]
    
    # Install each requirement
    success = True
    for req in requirements:
        req = req.strip()
        if not req or req.startswith('#'):
            continue
        
        print(f"\nInstalling: {req}")
        try:
            if 'flash-attn' in req.lower():
                # FlashAttention needs special handling
                print("Installing FlashAttention 2 (this may take several minutes)...")
                print("正在安装 FlashAttention 2（可能需要几分钟）...")
                result = subprocess.run(
                    [sys.executable, "-m", "pip", "install", req, "--no-build-isolation"],
                    capture_output=True,
                    text=True
                )
            else:
                result = subprocess.run(
                    [sys.executable, "-m", "pip", "install", req],
                    capture_output=True,
                    text=True
                )
            
            if result.returncode == 0:
                print(f"✓ Successfully installed: {req}")
            else:
                print(f"✗ Failed to install: {req}")
                print(f"Error: {result.stderr[:200]}")
                if 'flash-attn' in req.lower():
                    print("⚠ FlashAttention installation failed, but plugin will work without it")
                    print("⚠ FlashAttention 安装失败，但插件可以在没有它的情况下工作")
                else:
                    success = False
        except Exception as e:
            print(f"✗ Exception while installing {req}: {e}")
            if 'flash-attn' not in req.lower():
                success = False
    
    return success

def verify_installation():
    """Verify that critical dependencies are installed"""
    print("\n" + "="*60)
    print("Verifying installation...")
    print("验证安装...")
    print("="*60 + "\n")
    
    critical_packages = [
        "torch",
        "torchvision",
        "diffusers",
        "transformers",
        "peft",
        "omegaconf",
        "accelerate"
    ]
    
    optional_packages = [
        "flash_attn"
    ]
    
    all_ok = True
    
    for package in critical_packages:
        try:
            __import__(package)
            print(f"✓ {package} is installed")
        except ImportError:
            print(f"✗ {package} is NOT installed (required)")
            all_ok = False
    
    print()
    
    for package in optional_packages:
        try:
            module = __import__(package)
            version = getattr(module, "__version__", "unknown")
            print(f"✓ {package} {version} is installed (optional)")
        except ImportError:
            print(f"⚠ {package} is NOT installed (optional, for performance)")
    
    return all_ok

def main():
    print("="*60)
    print("HYPIR ComfyUI Plugin Installation")
    print("HYPIR ComfyUI 插件安装")
    print("="*60 + "\n")
    
    print(f"Python version: {sys.version}")
    print(f"Platform: {platform.platform()}\n")
    
    # Check CUDA
    cuda_compatible, cuda_version = check_cuda()
    
    # Ask user if they want to install FlashAttention
    skip_flash = False
    if cuda_compatible is False:
        print("\n⚠ Your GPU is not compatible with FlashAttention 2")
        print("⚠ 您的 GPU 不兼容 FlashAttention 2")
        response = input("\nSkip FlashAttention installation? (Y/n): ")
        skip_flash = response.strip().lower() != 'n'
    elif cuda_compatible is None:
        print("\n⚠ Could not detect CUDA compatibility")
        print("⚠ 无法检测 CUDA 兼容性")
        response = input("\nTry to install FlashAttention anyway? (y/N): ")
        skip_flash = response.strip().lower() != 'y'
    
    # Install dependencies
    success = install_dependencies(skip_flash_attention=skip_flash)
    
    if not success:
        print("\n✗ Some critical dependencies failed to install")
        print("✗ 一些关键依赖安装失败")
        print("Please check the error messages above and install manually")
        print("请查看上面的错误信息并手动安装")
        return 1
    
    # Verify installation
    if not verify_installation():
        print("\n✗ Installation verification failed")
        print("✗ 安装验证失败")
        return 1
    
    print("\n" + "="*60)
    print("✓ Installation completed successfully!")
    print("✓ 安装成功完成！")
    print("="*60)
    print("\nYou can now use the HYPIR plugin in ComfyUI")
    print("现在可以在 ComfyUI 中使用 HYPIR 插件了")
    
    if skip_flash or cuda_compatible is False:
        print("\n⚠ Note: FlashAttention was not installed")
        print("⚠ 注意：FlashAttention 未安装")
        print("The plugin will use standard attention (slower but works)")
        print("插件将使用标准注意力（较慢但可用）")
    
    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n\n✗ Installation cancelled by user")
        print("✗ 用户取消安装")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
        print(f"✗ 意外错误：{e}")
        sys.exit(1)
