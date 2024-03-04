# Release Note for Transformers v4.38.2

**Maintainer:** huggingface

**Repository:** transformers

## Version: v4.38.2

- Fixed backward compatibility issues with Llama and Gemma.
- Ensured performances are not affected by the new change of paradigm with ROPE.
- Fixed the ROPE computation to always be in float32.
- The causal_maskdtype was set to bool to reduce RAM usage.
- YOLOS had a regression issue.
- Fixed a bad rebase with transformers main for Gemma.
- Improved _update_causal_mask performance.
- Removed warning for T5 and Llama Tokenizer.
- Fixed torch export and slow downs in forward for Llama ROPE.
- RoPE lost precision for Llama / Gemma + Gemma logits.float().
- Patched YOLOS and other issues.
- Used torch.bool instead of torch.int64 for non-persistent causal mask buffer.<img src="https://img.shields.io/badge/PYTHON-black?style=for-the-badge&logo=python&logoColor=gold"/>
<img src="https://img.shields.io/badge/HTML-black?style=for-the-badge&logo=HTML5&logoColor=E34F26"/>
