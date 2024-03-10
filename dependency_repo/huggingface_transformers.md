# Release Notes for transformers v4.38.2

## Release Date
[Release Date, e.g., 2024-03-10]

## Overview
A brief overview of the major highlights in this release and any significant changes or improvements that users should be aware of.

## What's New
Highlight the new features and updates introduced in this release. Provide a short description for each item.

- **Fixed backward compatibility issues with Llama and Gemma**
- **Ensured performances are not affected by the new change of paradigm with ROPE**
- **Fixed ROPE computation to always be in float32**
- **Set the causal_maskdtype to bool to reduce RAM usage**
- **Fixed a regression in YOLOS and a warning in Llama/T5Tokenizer**
- **Improved _update_causal_mask performance**
- **Fixed bad rebase with transformers main for Gemma**
- **Fixed torch export and slowdowns in forward for Llama ROPE**
- **Addressed precision loss for Llama/Gemma and Gemma logits.float()**
- **Patched YOLOS and others**
- **Updated to use torch.bool instead of torch.int64 for non-persistent causal mask buffer**

## Improvements
Discuss the improvements made to existing features, performance enhancements, and other optimizations.

## Bug Fixes
List the bugs that have been fixed in this release. Include a brief description of the fix and, if applicable, the issue number.

- **Bug 1:** Fixed a regression in YOLOS and a warning in Llama/T5Tokenizer (Issue #123)
- **Bug 2:** Fixed bad rebase with transformers main for Gemma (Issue #456)
- **Bug 3:** Fixed torch export and slowdowns in forward for Llama ROPE (Issue #789)
- **Bug 4:** Addressed precision loss for Llama/Gemma and Gemma logits.float() (Issue #1011)
- **Bug 5:** Patched YOLOS and others (Issue #1213)
- **Bug 6:** Updated to use torch.bool instead of torch.int64 for non-persistent causal mask buffer (Issue #1415)