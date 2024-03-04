```markdown
# Release Notes - transformers v4.38.2

**Repository Owner:** huggingface  
**Repository:** transformers  
**Version:** v4.38.2

- Fixed backward compatibility issues with Llama and Gemma
- Ensured that performances are not affected by the new change of paradigm with ROPE
- Fixed the ROPE computation to always be in float32
- Set the causal_mask dtype to bool to reduce RAM usage
- Addressed regression in YOLOS and warning in Llama / T5Tokenizer
- Fixed bad rebase with transformers main
- Improved performance of _update_causal_mask
- Removed warning for T5 and Llama Tokenizer
- Fixed torch export and slowdowns in forward for Llama ROPE
- Addressed precision loss for Llama / Gemma + Gemma logits.float()
- Patched YOLOS and others
- Updated to use torch.bool instead of torch.int64 for non-persistent causal mask buffer
```  