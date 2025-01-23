# 🔐 Advanced PII Redaction Library

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

# 🔐 PII Redactor Library

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A robust, production-grade toolkit for sensitive data detection and anonymization across documents, emails, and structured text. Combines regex pattern matching with AI-powered entity recognition to safeguard personal information while preserving file integrity.

## 🌟 Key Features

### 📂 Multi-Format Support
- Process text files, Word documents, and PDFs without losing formatting

### 🔍 Hybrid Detection Engine
- 🕵️ **Regex Patterns**: 40+ built-in rules for emails, phones, IDs, financial data  
- 🧠 **AI/NLP Analysis**: spaCy-powered recognition of names, organizations, and contextual entities

### 🌍 Localization Ready
- 🇺🇸 English (SSN, credit cards)  
- 🇪🇸 Spanish (DNI, IBAN, localized entities)  
- 🛠 Custom locale templates

### 🏢 Enterprise-Grade Redaction
- Audit-ready JSON logs with exact match positions  
- Reversible anonymization via cryptographic hashing  
- Configurable masking characters (▰, █, X)

### ⚙ Customizable Pipeline
- YAML-based rule configurations  
- Plugin architecture for custom detectors  
- Model upgrades for industry-specific terminology

## 📋 Supported PII Types

| Category        | Examples                     | Validation            |
|-----------------|------------------------------|-----------------------|
| Identification  | SSN, DNI, NIE, Passport      | Format + Checksum     |
| Financial       | Credit Cards, IBAN           | Luhn Algorithm        |
| Contact         | Emails, Phone Numbers        | RFC/ITU Compliance    |
| Professional    | Names + Titles, Organizations| Contextual NLP        |

## 🛠 Use Cases

- 🔏 **Data Sanitization**: Prepare datasets for ML/Analytics  
- 📄 **Document Compliance**: GDPR/HIPAA-ready redaction  
- 🔐 **Secure Sharing**: Anonymize contracts, reports, emails  
- 🕵️ **Forensics**: Identify leaks in document repositories  

## 💡 Why This Library?

Unlike basic redaction tools, this solution:  
1. **Preserves original file layouts** (PDF/DOCX tables, formatting)  
2. **Detects indirect PII leaks** (e.g., "Dr. Smith at ABC Corp")  
3. **Scales from single documents** to batch processing  
4. **Future-proofs workflows** via customizable rules  

> **Developer Note**  
> 🔴 CLI currently in beta - full production stability coming in v2.0
## 🌟 Feature Overview

### 🔍 PII Detection Engine
**1. Pattern-Based Detection**  
Regular expression matching for:
- 📧 Emails: `\b[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+\b`
- 📞 Phone Numbers: International format support with country code detection
- 🆔 SSN: `\b(?!000|666|9\d{2})\d{3}-(?!00)\d{2}-(?!0000)\d{4}\b`
- 💳 Credit Cards: Luhn algorithm validation
- 🏦 IBAN (ES): Spanish bank account validation
- 🆔 DNI/NIE (ES): Spanish identity numbers

**2. NLP Entity Recognition**  
spaCy-powered detection for:
- 👤 Person Names: With honorific handling (Dr., Mr., etc.)
- 🏢 Organizations: With suffix detection (LLC, Inc, Corp)
- Multi-word entity grouping with context analysis

### 🛡 Redaction Capabilities
- █ Full-character redaction with configurable mask character
- 📝 Position-aware logging of all redactions
- 🔄 Bidirectional redaction reversal using operation logs
- 🧩 Intelligent overlap merging for nested matches
- 📂 Format-preserving redaction for:
  - 📄 Text files (.txt)
  - 📑 Word documents (.docx)
  - 📊 PDF documents (.pdf)

### 🌐 Localization Support
**en_US**:
- NER Model: `en_core_web_sm`
- Honorifics: Dr., Mr., Mrs., Ms., Prof.
- Organization Suffixes: LLC, Inc, Ltd, Corp, Co

**es_ES**:
- NER Model: `es_core_news_sm`
- Honorifics: Dr., Dra., Sr., Sra., Don, Doña
- Special Patterns: DNI, NIE, IBAN
- Organization Keywords: Empresa, Compañía, Corporación

### ⚙ Configuration System
```yaml
# custom_config.yml
patterns:
  custom_id: '\bID-\d{4}-[A-Z]{2}\b'  # Add new patterns
  credit_card: # Override existing patterns
    pattern: '\b\d{4}[\s-]*\d{4}[\s-]*\d{4}[\s-]*\d{4}\b'
    validation: luhn  # Enable Luhn check
    
locales:
  en_US:
    ner_model: en_core_web_md  # Upgrade model
    honorifics: [Chair., Rep.]  # Custom honorifics
```


📊 Redaction Logging
```json
[
  {
    "start": 45,
    "end": 60,
    "original": "john@example.com",
    "pii_type": "email"
  }
]
```

🚀 Installation
```python
# Base installation
pip install pii_redactor

# Required NLP models
python -m spacy download en_core_web_sm
python -m spacy download es_core_news_sm

# Optional dependencies
pip install pdfplumber python-docx reportlab
```

🛠 Usage Examples
## 🚀 Usage Examples (Preview)

*Full documentation coming in v1.1 release*

### 1️⃣ Configuration Management
```python
from pii_redactor.pii_redactor import PIIConfig

# Create custom config file
config_content = """
%%writefile custom_config.yml
locales:
  es_ES:
    patterns:
      dni: '\b\d{8}[A-Z]\b'
    ner_model: es_core_news_sm
"""

# Initialize with custom config
custom_config = PIIConfig("custom_config.yml")
print("🛠 Custom DNI Pattern:", custom_config.config['locales']['es_ES']['patterns']['dni'])
```

2️⃣ Multi-Format File Handling
```python
from pathlib import Path
from pii_redactor.pii_redactor import FileHandler

# Write test content to multiple formats
test_content = """John Doe <john@example.com>
Phone: +1 (555) 123-4567
SSN: 123-45-6789"""

for fmt in ['.txt', '.docx', '.pdf']:
    file_path = Path(f'document{fmt}')
    FileHandler.write(test_content, file_path)
    print(f"\n📁 {fmt} Preview:")
    print(FileHandler.read(file_path)[:100])  # First 100 characters
```

3️⃣ English PII Processing
```python
from pii_redactor.pii_redactor import PIIRedactor

# Initialize detector
redactor = PIIRedactor(locale='en_US')

# Detect and redact
text = """John Doe <john@example.com>
Phone: +1 (555) 123-4567
SSN: 123-45-6789
Card: 4111-1111-1111-1111"""
pii_data = redactor.detect_pii(text)

print("\n🔍 Detection Results:")
for pii_type, matches in pii_data.items():
    print(f"- {pii_type}: {len(matches)} matches")

redacted = redactor.redact_text(text, pii_data)
print("\n🔴 Redacted Text:", redacted)
```

4️⃣ Spanish PII Handling
```python
es_text = """Sr. Carlos García con DNI X1234567X
IBAN: ES12 3456 7890 1234 5678 9012
Trabaja en Empresa Ejemplo SL"""

# Spanish-specific processing
redactor_es = PIIRedactor(locale='es_ES')
pii_data = redactor_es.detect_pii(es_text)

print("\n🇪🇸 Spanish Detection:")
print("- DNI Found:", any('X1234567X' in dni for dni in pii_data.get('dni', [])))
print("- IBAN Found:", any('ES12' in iban for iban in pii_data.get('iban', [])))

redacted_es = redactor_es.redact_text(es_text, pii_data)
print("\n🔴 Redacted Spanish Text:\n", redacted_es)
```


5️⃣ Redaction Reversal
```python
from pii_redactor.pii_redactor import RedactionRecord

original = "Secret: 4111-1111-1111-1111"
redactor = PIIRedactor()

# Redact and log
redacted = redactor.redact_text(original, {'credit_card': ['4111-1111-1111-1111']})

# Reverse using log
restored = redactor.reverse_redaction(redacted, redactor.redaction_log)
print(f"\n⏮ Restoration Match: {original == restored}")  # True
```

6️⃣ Full Processing Pipeline
```python
from pathlib import Path
import json

input_file = Path("financial_report.docx")
output_file = Path("redacted_report.pdf")

# Process document
redactor = PIIRedactor()
result = redactor.process_file(input_file, output_file)

print("\n📊 Processing Report:")
print(f"- Detected {sum(len(v) for v in result.values())} PII instances")
print(f"- Generated {output_file}")

# Inspect log
log_file = output_file.with_suffix('.log.json')
with open(log_file) as f:
    print("\n📋 Redaction Log Preview:", json.load(f)[:2])
```


⌛ Coming Soon
### Full API documentation
### Detailed configuration guide
### Performance optimization tips
### Enterprise deployment strategies
### CLI stability improvements (v2.0)



⌨ CLI Interface (Beta)
```bash
# Basic redaction
pii_redact input.pdf output.pdf --locale es_ES

# Custom configuration
pii_redact sensitive.docx redacted.docx --config security.yml

# Redaction reversal
pii_redact redacted.txt restored.txt --reverse log.json

# Verbose output
pii_redact document.txt output.txt -v
```

## Full CLI stability coming in v2.0


🧩 Architecture
```yaml
graph TD
    A[Input File] --> B{File Handler}
    B -->|Text Extraction| C[PII Detector]
    C --> D[Regex Matcher]
    C --> E[NLP Analyzer]
    D --> F[Redaction Engine]
    E --> F
    F --> G[File Writer]
    G --> H[Redacted File]
    F --> I[Log Generator]
    I --> J[Redaction Log]
```


🤝 Contributing
### Report issues via GitHub Issues
### Develop features in dedicated branches
### Submit PRs with:
### Updated tests
### Documentation changes
### Type hints for new code



📜 License
## MIT License - See LICENSE for full details
