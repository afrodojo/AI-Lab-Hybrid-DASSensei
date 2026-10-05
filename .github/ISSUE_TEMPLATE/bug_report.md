name: 🐛 Bug Report
description: Create a report to help us fix a bug or execution error.
title: '[BUG]: '
labels: ['bug']
body:
  - type: textarea
    id: description
    attributes:
      label: Bug Description
      description: A clear description of the bug.
  - type: dropdown
    id: environment
    attributes:
      label: Execution Environment
      options:
        - Windows (CUDA)
        - macOS (Apple Silicon / Metal)
        - Linux (CUDA / ROCm)
        - Cloud Node (RunPod / Modal / Lambda)
