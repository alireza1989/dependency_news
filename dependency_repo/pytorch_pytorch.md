```markdown
# PyTorch 2.2.1 Release Notes

**Repository Owner:** PyTorch  
**Repository:** PyTorch  

- Fix missing OpenMP support on Apple Silicon binaries ([pytorch/builder#1697](https://github.com/pytorch/builder/issues/1697))
- Fix crash when mixing lazy and non-lazy tensors in one operation ([#117653](https://github.com/pytorch/pytorch/issues/117653))
- Fix PyTorch performance regression on Linux aarch64 ([pytorch/builder#1696](https://github.com/pytorch/builder/issues/1696))
- Fix silent correctness in DTensor_to_copyoperation ([#116426](https://github.com/pytorch/pytorch/issues/116426))
- Fix properly assigning param.grad_fn for next forward ([#116792](https://github.com/pytorch/pytorch/issues/116792))
- Ensure gradient clear out pending AsyncCollectiveTensor in FSDP Extension ([#116122](https://github.com/pytorch/pytorch/issues/116122))
- Fix processing unflatten tensor on compute stream in FSDP Extension ([#116559](https://github.com/pytorch/pytorch/issues/116559))
- Fix FSDPAssertionError on tensor subclass when setting sync_module_states=True ([#117336](https://github.com/pytorch/pytorch/issues/117336))
- Fix DCP state_dict cannot correctly find FQN when the leaf module is wrapped by FSDP ([#115592](https://github.com/pytorch/pytorch/issues/115592))
- Fix OOM when returning an AsyncCollectiveTensor by forcing gather_state_dict() to be synchronous with respect to the main stream ([#118197](https://github.com/pytorch/pytorch/issues/118197)) ([#119716](https://github.com/pytorch/pytorch/issues/119716))
- Fix Windows runtime torch.distributed.DistNetworkError: [WinError 32] The process cannot access the file because it is being used by another process ([#118860](https://github.com/pytorch/pytorch/issues/118860))
- Update supported python versions in package description ([#119743](https://github.com/pytorch/pytorch/issues/119743))
- Fix SIGILL crash during import torch on CPUs that do not support SSE4.1 ([#116623](https://github.com/pytorch/pytorch/issues/116623))
- Fix DCP RuntimeError in get_state_dict and set_state_dict ([#119573](https://github.com/pytorch/pytorch/issues/119573))
- Fixes for HSDP + TP integration with device_mesh ([#112435](https://github.com/pytorch/pytorch/issues/112435)) ([#118620](https://github.com/pytorch/pytorch/issues/118620)) ([#119064](https://github.com/pytorch/pytorch/issues/119064)) ([#118638](https://github.com/pytorch/pytorch/issues/118638)) ([#119481](https://github.com/pytorch/pytorch/issues/119481))
- Fix numerical error with mixed mon NVIDIA V100 ([#118591](https://github.com/pytorch/pytorch/issues/118591))
- Fix RuntimeError when using SymInt input invariant when splitting graphs ([#117406](https://github.com/pytorch/pytorch/issues/117406))
- Fix compile DTensor.from_local in trace_rule look up ([#119659](https://github.com/pytorch/pytorch/issues/119659))
- Improve torch.compile integration with CUDA-11.8 binaries ([#119750](https://github.com/pytorch/pytorch/issues/119750))

*Release tracker #119295 contains all relevant pull requests related to this release as well as links to related issues.*
```
```