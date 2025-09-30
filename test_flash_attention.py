#!/usr/bin/env python3
"""
FlashAttention 2 Test Script
FlashAttention 2 测试脚本

This script tests if FlashAttention 2 is properly installed and working.
本脚本测试 FlashAttention 2 是否正确安装和工作。
"""

import sys
import os

def test_flash_attention_import():
    """Test if FlashAttention can be imported"""
    print("="*60)
    print("Testing FlashAttention 2 Import")
    print("测试 FlashAttention 2 导入")
    print("="*60 + "\n")
    
    try:
        import flash_attn
        version = getattr(flash_attn, "__version__", "unknown")
        print(f"✓ FlashAttention imported successfully")
        print(f"✓ Version: {version}")
        return True
    except ImportError as e:
        print(f"✗ Failed to import FlashAttention: {e}")
        print("FlashAttention is not installed or not compatible with your system")
        print("FlashAttention 未安装或与您的系统不兼容")
        return False

def test_cuda_availability():
    """Test CUDA availability and GPU compatibility"""
    print("\n" + "="*60)
    print("Testing CUDA and GPU")
    print("测试 CUDA 和 GPU")
    print("="*60 + "\n")
    
    try:
        import torch
        
        if not torch.cuda.is_available():
            print("✗ CUDA is not available")
            print("FlashAttention requires CUDA GPU")
            print("FlashAttention 需要 CUDA GPU")
            return False
        
        print(f"✓ CUDA is available")
        print(f"✓ CUDA version: {torch.version.cuda}")
        print(f"✓ PyTorch version: {torch.__version__}")
        
        device_count = torch.cuda.device_count()
        print(f"✓ Number of GPUs: {device_count}\n")
        
        for i in range(device_count):
            device_name = torch.cuda.get_device_name(i)
            compute_cap = torch.cuda.get_device_capability(i)
            memory = torch.cuda.get_device_properties(i).total_memory / 1024**3
            
            print(f"GPU {i}:")
            print(f"  Name: {device_name}")
            print(f"  Compute Capability: {compute_cap[0]}.{compute_cap[1]}")
            print(f"  Memory: {memory:.2f} GB")
            
            if compute_cap >= (7, 5):
                print(f"  ✓ Compatible with FlashAttention 2")
            else:
                print(f"  ✗ NOT compatible with FlashAttention 2 (requires >= 7.5)")
            print()
        
        return True
        
    except ImportError:
        print("✗ PyTorch is not installed")
        return False

def test_hypir_integration():
    """Test FlashAttention integration with HYPIR"""
    print("="*60)
    print("Testing HYPIR Integration")
    print("测试 HYPIR 集成")
    print("="*60 + "\n")
    
    # Add HYPIR to path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    hypir_path = os.path.join(current_dir, "HYPIR")
    if hypir_path not in sys.path:
        sys.path.append(hypir_path)
    
    try:
        from HYPIR.enhancer.base import BaseEnhancer, FLASH_ATTENTION_AVAILABLE, FLASH_ATTENTION_VERSION
        
        print(f"✓ HYPIR enhancer imported successfully")
        print(f"✓ FlashAttention available in HYPIR: {FLASH_ATTENTION_AVAILABLE}")
        
        if FLASH_ATTENTION_AVAILABLE:
            print(f"✓ FlashAttention version detected: {FLASH_ATTENTION_VERSION}")
        else:
            print("⚠ FlashAttention not available in HYPIR")
            print("Plugin will use standard attention")
            print("插件将使用标准注意力")
        
        return True
        
    except Exception as e:
        print(f"✗ Failed to test HYPIR integration: {e}")
        return False

def test_attention_processor():
    """Test if attention processor can be loaded"""
    print("\n" + "="*60)
    print("Testing Attention Processor")
    print("测试注意力处理器")
    print("="*60 + "\n")
    
    try:
        from diffusers.models.attention_processor import AttnProcessor2_0
        print("✓ AttnProcessor2_0 imported successfully")
        print("This will be used for optimized attention")
        print("这将用于优化的注意力计算")
        return True
    except ImportError as e:
        print(f"✗ Failed to import AttnProcessor2_0: {e}")
        return False

def run_performance_test():
    """Optional: Run a simple performance test"""
    print("\n" + "="*60)
    print("Performance Test (Optional)")
    print("性能测试（可选）")
    print("="*60 + "\n")
    
    response = input("Run a simple performance test? This will use GPU memory. (y/N): ")
    if response.strip().lower() != 'y':
        print("Skipped performance test")
        return True
    
    try:
        import torch
        import time
        
        if not torch.cuda.is_available():
            print("✗ CUDA not available, cannot run performance test")
            return False
        
        print("\nRunning attention computation test...")
        print("运行注意力计算测试...\n")
        
        device = torch.device("cuda")
        batch_size = 2
        seq_len = 1024
        hidden_dim = 768
        
        # Create dummy tensors
        q = torch.randn(batch_size, seq_len, hidden_dim, device=device, dtype=torch.float16)
        k = torch.randn(batch_size, seq_len, hidden_dim, device=device, dtype=torch.float16)
        v = torch.randn(batch_size, seq_len, hidden_dim, device=device, dtype=torch.float16)
        
        # Warmup
        _ = torch.nn.functional.scaled_dot_product_attention(q, k, v)
        torch.cuda.synchronize()
        
        # Benchmark
        num_iterations = 10
        start_time = time.time()
        for _ in range(num_iterations):
            _ = torch.nn.functional.scaled_dot_product_attention(q, k, v)
        torch.cuda.synchronize()
        end_time = time.time()
        
        avg_time = (end_time - start_time) / num_iterations * 1000
        print(f"✓ Average attention computation time: {avg_time:.2f} ms")
        print(f"✓ 平均注意力计算时间：{avg_time:.2f} 毫秒")
        
        # Check if FlashAttention was used
        if torch.backends.cuda.flash_sdp_enabled():
            print("✓ FlashAttention backend is enabled")
            print("✓ FlashAttention 后端已启用")
        else:
            print("⚠ FlashAttention backend not used (may use other optimized backend)")
            print("⚠ 未使用 FlashAttention 后端（可能使用其他优化后端）")
        
        return True
        
    except Exception as e:
        print(f"✗ Performance test failed: {e}")
        return False

def main():
    print("\n" + "="*60)
    print("FlashAttention 2 Test Suite")
    print("FlashAttention 2 测试套件")
    print("="*60 + "\n")
    
    results = []
    
    # Run tests
    results.append(("FlashAttention Import", test_flash_attention_import()))
    results.append(("CUDA and GPU", test_cuda_availability()))
    results.append(("HYPIR Integration", test_hypir_integration()))
    results.append(("Attention Processor", test_attention_processor()))
    results.append(("Performance Test", run_performance_test()))
    
    # Summary
    print("\n" + "="*60)
    print("Test Summary")
    print("测试总结")
    print("="*60 + "\n")
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{status}: {test_name}")
    
    print(f"\nPassed: {passed}/{total}")
    print(f"通过：{passed}/{total}")
    
    if results[0][1] and results[1][1] and results[2][1]:
        print("\n✓ FlashAttention 2 is ready to use!")
        print("✓ FlashAttention 2 可以使用了！")
        return 0
    elif results[2][1]:
        print("\n⚠ FlashAttention 2 is not available, but HYPIR will work with standard attention")
        print("⚠ FlashAttention 2 不可用，但 HYPIR 可以使用标准注意力工作")
        return 0
    else:
        print("\n✗ Some tests failed. Please check the errors above.")
        print("✗ 一些测试失败。请检查上面的错误。")
        return 1

if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n\nTest cancelled by user")
        print("用户取消测试")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
