# Release Notes for pytorch-lightning v2.2.1

## Release Date
[Release Date, 
    e.g., 2024-03-10]

## Overview
A brief overview of the major highlights in this release and any significant changes or improvements that users should be aware of.

### What's New
Highlight the new features and updates introduced in this release. Provide a short description for each item.

- **PyTorch:**
  - Fixed issue with CSVLogger appending to file from previous run when version is set manually
  - Fixed divisibility check for Trainer.accumulate_grad_batches and Trainer.log_every_n_steps in ThroughputMonitor
  - Fixed support for Remote Stop and Remote Abort with NeptuneLogger
  - Fixed infinite recursion error in precision plugin graveyard

- **Fabric:**
  - Fixed issue with CSVLogger appending to file from previous run

## Contributors
- @Raalsky
- @awaelchli
- @carmocca
- @Borda

For full changelog, refer to version 2.2.0 post.