import pytest
from pii_redactor import PIIRedactor

def test_email_redaction():
    redactor = PIIRedactor()
    text = "Contact: john@example.com"
    pii_data = redactor.detect_pii(text)
    assert "emails" in pii_data
    assert len(pii_data["emails"]) == 1

def test_phone_redaction():
    redactor = PIIRedactor()
    text = "Call +1 (555) 123-4567"
    pii_data = redactor.detect_pii(text)
    assert "phones" in pii_data
    assert len(pii_data["phones"]) == 1