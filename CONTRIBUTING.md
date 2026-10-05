# Contributing to AI-Lab-Hybrid-DASSensei

Thank you for helping improve AI-Lab-Hybrid-DASSensei! We welcome contributions from beginners, independent researchers, and academic/enterprise institutions.

## Ways to Contribute

- **Beginners:** Documentation fixes, bug reporting, adding tutorial examples, or testing on different local hardware.
- **Researchers:** Adding benchmark datasets, fine-tuning loss optimizations, custom quantization techniques.
- **Institutions & Security Experts:** Enhancing NeMo Guardrail rules, PII sanitization filters, or adding cloud orchestration templates.

## Getting Started

1. Fork the repository and clone your fork locally.
2. Set up your virtual environment:
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   python -m pip install -r requirements.txt
3. Run local security checks before submitting code:
   python security/guardrail_check.py
   python scripts/01_prep_dataset.py
   python scripts/02_test_local.py
4. Create a descriptive branch and submit a Pull Request.
