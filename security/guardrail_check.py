import re
import sys
import os

def sanitize_input(text: str) -> dict:
    """
    Scans text for PII leaks, prompt injection attacks, and dangerous system overrides.
    """
    pii_patterns = {
        "email": r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
        "api_key": r'(hf_[a-zA-Z0-9]{32,}|sk-[a-zA-Z0-9]{32,})',
        "ssn": r'\b\d{3}-\d{2}-\d{4}\b'
    }
    
    injection_keywords = [
        "ignore previous instructions",
        "system prompt override",
        "jailbreak",
        "DAN mode",
        "bypass safety"
    ]
    
    findings = []
    
    # Check for PII
    for pii_type, pattern in pii_patterns.items():
        if re.search(pattern, text):
            findings.append(f"PII Leak Detected ({pii_type})")
            
    # Check for Prompt Injections
    for phrase in injection_keywords:
        if phrase.lower() in text.lower():
            findings.append(f"Prompt Injection Attack Detected ('{phrase}')")
            
    is_safe = len(findings) == 0
    return {"is_safe": is_safe, "violations": findings}

if __name__ == "__main__":
    sample = "Testing dataset row for safety compliance."
    result = sanitize_input(sample)
    if not result["is_safe"]:
        print(f"❌ Guardrail Security Violation: {result['violations']}")
        sys.exit(1)
    else:
        print("✅ Input cleared security guardrails.")
