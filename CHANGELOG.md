# Changelog
# 更新日志

All notable changes to this project will be documented in this file.
本文件记录项目的所有重要变更。

## [Unreleased] - 2025-09-30

### Added
### 新增

- **FlashAttention 2.8.3 Support**: Integrated FlashAttention 2 for 2-3x faster inference on compatible GPUs
- **FlashAttention 2.8.3 支持**：集成 FlashAttention 2，在兼容 GPU 上实现 2-3 倍推理速度提升
- `use_flash_attention` parameter in HYPIRAdvancedRestoration node to toggle FlashAttention
- HYPIRAdvancedRestoration 节点中的 `use_flash_attention` 参数，用于切换 FlashAttention
- Automatic fallback to standard attention if FlashAttention is not available
- 当 FlashAttention 不可用时自动回退到标准注意力
- Installation script (`install.py`) for easier dependency management
- 安装脚本（`install.py`）以便更轻松地管理依赖
- Comprehensive FlashAttention documentation (`FLASHATTENTION.md`)
- 完整的 FlashAttention 文档（`FLASHATTENTION.md`）
- GPU compatibility checking and reporting
- GPU 兼容性检查和报告

### Changed
### 更改

- Updated `requirements.txt` to include `flash-attn==2.8.3`
- 更新 `requirements.txt` 以包含 `flash-attn==2.8.3`
- Enhanced `BaseEnhancer` class to support FlashAttention parameter
- 增强 `BaseEnhancer` 类以支持 FlashAttention 参数
- Modified `SD2Enhancer` to enable FlashAttention for UNet and text encoder models
- 修改 `SD2Enhancer` 以为 UNet 和文本编码器模型启用 FlashAttention
- Updated README with FlashAttention installation and usage instructions
- 更新 README，添加 FlashAttention 安装和使用说明
- Improved status messages to show FlashAttention state
- 改进状态消息以显示 FlashAttention 状态

### Technical Details
### 技术细节

- FlashAttention is automatically detected at import time
- FlashAttention 在导入时自动检测
- Uses `AttnProcessor2_0` from diffusers for optimized attention
- 使用 diffusers 的 `AttnProcessor2_0` 实现优化的注意力
- Compatible with NVIDIA GPUs with compute capability >= 7.5
- 兼容计算能力 >= 7.5 的 NVIDIA GPU
- No breaking changes to existing workflows
- 对现有工作流无破坏性更改

## [Previous Versions]
## [以前的版本]

### Initial Release
### 初始版本

- Basic HYPIR image restoration functionality
- 基本的 HYPIR 图像修复功能
- Support for Stable Diffusion 2.1 base model
- 支持 Stable Diffusion 2.1 基础模型
- Advanced parameter controls (model_t, coeff_t, lora_rank, etc.)
- 高级参数控制（model_t、coeff_t、lora_rank 等）
- Automatic model downloading from HuggingFace and OpenXLab
- 从 HuggingFace 和 OpenXLab 自动下载模型
- Batch processing support
- 批处理支持
- Upscaling capabilities (1x-8x)
- 放大功能（1x-8x）
- Tiled VAE processing for large images
- 大图像的分块 VAE 处理
