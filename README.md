# 🎣 Phishing Email Detector — Threat Intelligence Tool

> A Python-based Blue Team cybersecurity tool that automatically analyzes emails for phishing indicators, detects suspicious domains, malicious links, dangerous attachments, and social engineering tactics — replicating real-world SOC L1 analyst email triage workflows used in enterprise security operations.

## 🎯 Why This Project?
Phishing attacks account for over 90% of all cyber attacks worldwide. In a real SOC environment, analysts manually review hundreds of emails daily to detect threats. This tool automates that process — demonstrating core Blue Team skills including threat detection, risk scoring, and incident reporting.

## ⚡ Key Features
- Detects phishing keywords and social engineering tactics
- Identifies suspicious sender domains (typosquatting)
- Flags malicious links and unsecure HTTP connections
- Detects dangerous attachments (.exe, .zip, .bat, .js, .vbs)
- Assigns automated risk scores with 5 severity levels
- Generates detailed threat intelligence reports saved as `.txt`
- Simulates real SOC L1 email triage workflows

## 🚨 Threat Detection Engine
| Threat Type | Detection Method | Severity |
|-------------|-----------------|----------|
| Phishing Keywords | urgency, winner, verify, suspended... | HIGH |
| Suspicious Domain | typosquatting (paypa1, g00gle...) | CRITICAL |
| Malicious Links | HTTP links, suspicious domains | HIGH |
| Dangerous Attachments | .exe, .zip, .bat, .js, .vbs | CRITICAL |
| Social Engineering | act now, limited time, free... | MEDIUM |
| Numbers in Sender | promo123@domain.com | MEDIUM |

## 📊 Risk Scoring System
| Score | Risk Level |
|-------|-----------|
| 0 | ✅ SAFE |
| 1-3 | 🟡 LOW RISK |
| 4-7 | 🟠 MEDIUM RISK |
| 8-12 | 🔴 HIGH RISK |
| 13+ | 🚨 CRITICAL - PHISHING DETECTED |

## 🛠️ Tools & Technologies
- Python 3
- Regex (re module) — pattern matching for threat detection
- Datetime module — timestamp generation
- File I/O — automated report generation

## 🚀 How To Run

### 1. Clone the repository
```bash
git clone https://github.com/sousou1999406/phishing-detector
cd phishing-detector
```

### 2. Run the tool
```bash
py phishing_detector.py
```

### 3. Check the report
```bash
cat phishing_report.txt
```

## 📸 Screenshots

### Critical Phishing Detected
<img width="1189" height="859" alt="image" src="https://github.com/user-attachments/assets/4dd08010-5d77-41e7-a697-40ddda23cff3" />
<img width="982" height="252" alt="image" src="https://github.com/user-attachments/assets/99d0c2a3-9788-4412-96b9-1ea2988684d9" />

### Safe Email
<img width="1126" height="853" alt="image" src="https://github.com/user-attachments/assets/840a72c1-0188-4bda-abb5-94c512c2fa01" />

## 📊 Example Output
```
============================================================

EMAIL #1 ANALYSIS REPORT

Generated: 2026-06-28 20:11:22
Subject: URGENT: Your account has been suspended!

From: security@paypa1.com

Risk Score: 31

Risk Level: CRITICAL - PHISHING DETECTED
Findings:

[!] Suspicious keyword in subject: 'urgent'

[!] Suspicious sender domain: paypa1.com

[!] Phishing keyword in body: 'click here'

[CRITICAL] Suspicious link: http://paypa1.com/verify

[CRITICAL] Suspicious attachment: update.exe
```
## 🔗 Related SOC Skills
- Email Threat Analysis & Triage
- Phishing Investigation & Detection
- Threat Intelligence Reporting
- Social Engineering Awareness
- Incident Documentation

## 📁 Project Structure
phishing-detector/

├── phishing_detector.py    # Main detection engine

├── phishing_report.txt     # Auto-generated threat report

├── phishing_critical.png   # Screenshot - phishing detected

├── phishing_safe.png       # Screenshot - safe email

└── README.md               # Project documentation

## ⚠️ Disclaimer
This tool is for **educational purposes only**.  
Built to simulate real SOC analyst workflows and demonstrate Blue Team cybersecurity skills.  
Do not use on systems without explicit permission.

## 👩‍💻 Author
**Soukaina Douazi** — Cybersecurity Student | SOC Analyst in Training  
📍 Casablanca, Morocco  
🔗 [LinkedIn](https://linkedin.com/in/soukaina-douazi)  
🔗 [GitHub](https://github.com/sousou1999406)
