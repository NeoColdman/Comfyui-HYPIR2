# FlashAttention 2 Setup Quick Guide
# FlashAttention 2 快速设置指南

## Quick Start
## 快速开始

### Windows Users
### Windows 用户

1. Open Command Prompt or PowerShell in the plugin directory:
1. 在插件目录中打开命令提示符或 PowerShell：
   ```
   cd ComfyUI\custom_nodes\Comfyui-HYPIR
   ```

2. Run the installation batch file:
2. 运行安装批处理文件：
   ```
   install.bat
   ```

### Linux/Mac Users
### Linux/Mac 用户

1. Open terminal in the plugin directory:
1. 在插件目录中打开终端：
   ```
   cd ComfyUI/custom_nodes/Comfyui-HYPIR
   ```

2. Make the script executable and run it:
2. 使脚本可执行并运行：
   ```
   chmod +x install.sh
   ./install.sh
   ```

   Or use Python directly:
   或直接使用 Python：
   ```
   python3 install.py
   ```

## What Gets Installed
## 将安装什么

The installation script will:
安装脚本将：

1. ✓ Check your system for CUDA and GPU compatibility
1. ✓ 检查系统的 CUDA 和 GPU 兼容性
2. ✓ Install all required dependencies from `requirements.txt`
2. ✓ 从 `requirements.txt` 安装所有必需的依赖
3. ✓ Attempt to install FlashAttention 2.8.3 (if compatible)
3. ✓ 尝试安装 FlashAttention 2.8.3（如果兼容）
4. ✓ Verify the installation
4. ✓ 验证安装
5. ✓ Provide feedback on what was installed
5. ✓ 提供安装内容的反馈

## Testing FlashAttention
## 测试 FlashAttention

After installation, test if FlashAttention is working:
安装后，测试 FlashAttention 是否工作：

```bash
python test_flash_attention.py
```

This will:
这将：
- Check if FlashAttention is installed
- 检查 FlashAttention 是否已安装
- Verify GPU compatibility
- 验证 GPU 兼容性
- Test integration with HYPIR
- 测试与 HYPIR 的集成
- Optionally run a performance benchmark
- 可选运行性能基准测试

## GPU Compatibility Check
## GPU 兼容性检查

To quickly check if your GPU supports FlashAttention:
快速检查您的 GPU 是否支持 FlashAttention：

```python
import torch
if torch.cuda.is_available():
    cap = torch.cuda.get_device_capability()
    print(f"GPU: {torch.cuda.get_device_name()}")
    print(f"Compute Capability: {cap[0]}.{cap[1]}")
    print(f"FlashAttention Compatible: {cap >= (7, 5)}")
```

### Compatible GPUs (Compute Capability >= 7.5)
### 兼容的 GPU（计算能力 >= 7.5）

✅ **NVIDIA RTX Series:**
- RTX 2060, 2070, 2080 (all variants)
- RTX 3060, 3070, 3080, 3090 (all variants)
- RTX 4060, 4070, 4080, 4090

✅ **NVIDIA Professional:**
- RTX A4000, A5000, A6000
- A100, A10, A40
- H100, H200

❌ **NOT Compatible (Compute Capability < 7.5):**
- GTX 10 series (1050, 1060, 1070, 1080)
- GTX 16 series (1650, 1660)
- Titan V, Tesla V100

## Manual FlashAttention Installation
## 手动安装 FlashAttention

If automatic installation fails, try:
如果自动安装失败，请尝试：

```bash
# Install with no-build-isolation flag
pip install flash-attn==2.8.3 --no-build-isolation

# Or with verbose output to see errors
pip install flash-attn==2.8.3 --no-build-isolation -v
```

### Common Installation Issues
### 常见安装问题

**Issue 1: CUDA version mismatch**
**问题 1：CUDA 版本不匹配**

```
Error: CUDA version X.X does not match PyTorch CUDA version Y.Y
```

**Solution**: Ensure your CUDA Toolkit version matches PyTorch's CUDA version
**解决方案**：确保 CUDA Toolkit 版本与 PyTorch 的 CUDA 版本匹配

```bash
python -c "import torch; print(torch.version.cuda)"
nvcc --version
```

**Issue 2: Compiler not found**
**问题 2：找不到编译器**

```
Error: Microsoft Visual C++ 14.0 or greater is required (Windows)
Error: gcc/g++ not found (Linux)
```

**Solution Windows**: Install Visual Studio Build Tools
**Windows 解决方案**：安装 Visual Studio 生成工具
- Download from: https://visualstudio.microsoft.com/downloads/
- Select "Desktop development with C++"
- 从此处下载：https://visualstudio.microsoft.com/downloads/
- 选择"使用 C++ 的桌面开发"

**Solution Linux**: Install build essentials
**Linux 解决方案**：安装构建必需品
```bash
sudo apt-get install build-essential
```

**Issue 3: Out of memory during compilation**
**问题 3：编译期间内存不足**

```
Error: ... killed (signal 9)
```

**Solution**: Increase system swap space or compile on a machine with more RAM
**解决方案**：增加系统交换空间或在具有更多 RAM 的机器上编译

## Using Without FlashAttention
## 不使用 FlashAttention

If you can't install FlashAttention, the plugin will still work perfectly:
如果无法安装 FlashAttention，插件仍可完美运行：

1. Remove `flash-attn==2.8.3` from `requirements.txt`
1. 从 `requirements.txt` 中删除 `flash-attn==2.8.3`
2. Install other dependencies: `pip install -r requirements.txt`
2. 安装其他依赖：`pip install -r requirements.txt`
3. Set `use_flash_attention=False` in the node (or it will auto-disable)
3. 在节点中设置 `use_flash_attention=False`（或将自动禁用）

The plugin will automatically fall back to standard attention mechanism.
插件将自动回退到标准注意力机制。

## Performance Expectations
## 性能预期

### With FlashAttention 2 (RTX 4090)
### 使用 FlashAttention 2（RTX 4090）

- **512x512 → 1024x1024**: ~6 seconds
- **1024x1024 → 2048x2048**: ~25 seconds
- **Speedup**: 2-3x faster than standard attention
- **加速**：比标准注意力快 2-3 倍

### Without FlashAttention
### 不使用 FlashAttention

- **512x512 → 1024x1024**: ~15 seconds
- **1024x1024 → 2048x2048**: ~60 seconds
- Still produces identical quality results
- 仍产生相同质量的结果

## Verification Checklist
## 验证检查清单

After installation, verify:
安装后验证：

- [ ] All dependencies installed: `pip list | grep -E "torch|diffusers|transformers|flash-attn"`
- [ ] 所有依赖已安装：`pip list | grep -E "torch|diffusers|transformers|flash-attn"`
- [ ] CUDA is available: `python -c "import torch; print(torch.cuda.is_available())"`
- [ ] CUDA 可用：`python -c "import torch; print(torch.cuda.is_available())"`
- [ ] GPU is compatible: `python test_flash_attention.py`
- [ ] GPU 兼容：`python test_flash_attention.py`
- [ ] Plugin loads in ComfyUI without errors
- [ ] 插件在 ComfyUI 中正常加载无错误
- [ ] Node shows "FlashAttention: enabled" in output
- [ ] 节点输出显示"FlashAttention: enabled"

## Getting Help
## 获取帮助

If you encounter issues:
如果遇到问题：

1. Run the test script: `python test_flash_attention.py`
1. 运行测试脚本：`python test_flash_attention.py`
2. Check the console output for error messages
2. 检查控制台输出的错误消息
3. Review [FLASHATTENTION.md](FLASHATTENTION.md) for detailed documentation
3. 查看 [FLASHATTENTION.md](FLASHATTENTION.md) 获取详细文档
4. Check [TROUBLESHOOTING](#common-installation-issues) section
4. 查看[故障排查](#common-installation-issues)部分
5. Report issues on GitHub with test script output
5. 在 GitHub 上报告问题并附上测试脚本输出

## Additional Resources
## 其他资源

- FlashAttention paper: https://arxiv.org/abs/2307.08691
- FlashAttention GitHub: https://github.com/Dao-AILab/flash-attention
- HYPIR project: https://github.com/XPixelGroup/HYPIR
- Compute Capability list: https://developer.nvidia.com/cuda-gpus
