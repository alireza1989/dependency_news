# Release Notes for PyTorch 2.2.1

## Release Date
2024-03-10

## Overview
This release includes several bug fixes and improvements. 

## What's New
- **Fix missing OpenMP support on Apple Silicon binaries**
- **Fix crash when mixing lazy and non-lazy tensors in one operation**
- **Fix PyTorch performance regression on Linux aarch64**

## Improvements
- **Ensure gradient clear out pending AsyncCollectiveTensor in FSDP Extension**
- **Improve torch.compile integration with CUDA-11.8 binaries**

## Bug Fixes
- **Fix silent correctness in DTensor_to_copy operation**
- **Fix properly assigning param.grad_fn for next forward**
- **Fix processing unflatten tensor on compute stream in FSDP Extension**
- **Fix FSDP AssertionError on tensor subclass when setting sync_module_states=True**
- **Fix OOM when returning a AsyncCollectiveTensor by forcing gather_state_dict() to be synchronous with respect to the main stream**
- **Fix Windows runtime torch.distributed.DistNetworkError: [WinError 32] The process cannot access the file because it is being used by another process**
- **Update supported python versions in package description**
- **Fix SIGILL crash during import torch on CPUs that do not support SSE4.1**
- **Fix DCP RuntimeError in get_state_dict and set_state_dict**
- **Fixes for HSDP + TP integration with device_mesh**
- **Fix numerical error with mixed mmon NVIDIA V100**
- **Fix RuntimeError when using SymInt input invariant when splitting graphs**
- **Fix compile DTensor.from_local in trace_rule_look up**