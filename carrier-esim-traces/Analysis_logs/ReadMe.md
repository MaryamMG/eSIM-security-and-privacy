# APDU and Certificate Extraction Scripts

This folder contains two Python scripts for analyzing logs from eSIM procedures.

---

## 1. `extract_apdu_commands.py`

**Purpose**:  
Parses `logcat` output to extract and decode APDU commands sent during eSIM installation.

**Key Features**:
- Searches for lines containing `Send: ApduCommand`
- Extracts the `cmd=...` APDU payload
- Attempts to decode:
  - As UTF-8 for readability

---

## 2. `extract_certs.py`

**Purpose**:  
Identifies and extracts lines from the log that mention certificates.

**Key Features**:
- Filters lines with `"cert"` in them
- Extracts and logs those lines for later inspection


---

## Requirements

- Python 3
- `pyasn1` (for ASN.1 decoding)

```bash
pip install pyasn1

