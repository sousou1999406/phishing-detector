import re
import datetime

# Phishing indicators
PHISHING_KEYWORDS = [
    'urgent', 'immediately', 'verify your account', 'suspended',
    'click here', 'confirm your password', 'winner', 'congratulations',
    'free', 'limited time', 'act now', 'expires', 'unusual activity',
    'security alert', 'update your information', 'validate'
]

SUSPICIOUS_DOMAINS = [
    'paypa1.com', 'arnazone.com', 'g00gle.com', 'faceb00k.com',
    'secure-bank.xyz', 'account-verify.net', 'login-secure.info'
]

SUSPICIOUS_EXTENSIONS = ['.exe', '.zip', '.rar', '.bat', '.js', '.vbs']

def analyze_email(subject, sender, body, links=[]):
    score = 0
    findings = []

    # Check subject
    for keyword in PHISHING_KEYWORDS:
        if keyword.lower() in subject.lower():
            score += 2
            findings.append(f"[!] Suspicious keyword in subject: '{keyword}'")

    # Check sender
    for domain in SUSPICIOUS_DOMAINS:
        if domain in sender.lower():
            score += 5
            findings.append(f"[!] Suspicious sender domain: {domain}")

    if re.search(r'\d+', sender.split('@')[0] if '@' in sender else sender):
        score += 2
        findings.append(f"[!] Numbers in sender name: {sender}")

    # Check body
    for keyword in PHISHING_KEYWORDS:
        if keyword.lower() in body.lower():
            score += 1
            findings.append(f"[!] Phishing keyword in body: '{keyword}'")

    # Check links
    for link in links:
        if re.search(r'http://', link):
            score += 2
            findings.append(f"[!] Unsecure HTTP link: {link}")
        for domain in SUSPICIOUS_DOMAINS:
            if domain in link:
                score += 5
                findings.append(f"[CRITICAL] Suspicious link detected: {link}")
        for ext in SUSPICIOUS_EXTENSIONS:
            if link.endswith(ext):
                score += 5
                findings.append(f"[CRITICAL] Suspicious attachment: {link}")

    # Risk level
    if score == 0:
        risk = "SAFE"
    elif score <= 3:
        risk = "LOW RISK"
    elif score <= 7:
        risk = "MEDIUM RISK"
    elif score <= 12:
        risk = "HIGH RISK"
    else:
        risk = "CRITICAL - PHISHING DETECTED"

    return score, risk, findings

def print_report(email_num, subject, sender, score, risk, findings):
    print("=" * 60)
    print(f"EMAIL #{email_num} ANALYSIS REPORT")
    print(f"Generated: {datetime.datetime.now()}")
    print("=" * 60)
    print(f"Subject: {subject}")
    print(f"From: {sender}")
    print(f"Risk Score: {score}")
    print(f"Risk Level: {risk}")
    print("-" * 60)
    if findings:
        print("Findings:")
        for f in findings:
            print(f"  {f}")
    else:
        print("  No suspicious indicators found.")
    print("=" * 60)

    with open("phishing_report.txt", "a", encoding="utf-8") as f:
        f.write(f"\nEMAIL #{email_num}\n")
        f.write(f"Subject: {subject}\n")
        f.write(f"From: {sender}\n")
        f.write(f"Risk Score: {score}\n")
        f.write(f"Risk Level: {risk}\n")
        for finding in findings:
            f.write(f"  {finding}\n")
        f.write("=" * 60 + "\n")

# Test emails
emails = [
    {
        "subject": "URGENT: Your account has been suspended!",
        "sender": "security@paypa1.com",
        "body": "Click here immediately to verify your account or it will be deleted.",
        "links": ["http://paypa1.com/verify", "http://login-secure.info/update.exe"]
    },
    {
        "subject": "Meeting tomorrow at 10am",
        "sender": "colleague@company.com",
        "body": "Hi, just a reminder about our meeting tomorrow.",
        "links": ["https://zoom.us/meeting/123"]
    },
    {
        "subject": "Congratulations! You are a winner!",
        "sender": "promo123@free-gifts.xyz",
        "body": "Act now! Limited time offer. Claim your free prize immediately!",
        "links": ["http://free-gifts.xyz/claim.zip"]
    }
]

print("PHISHING EMAIL DETECTOR")
print("Cybersecurity Tool by Soukaina Douazi")
print("Analyzing emails...\n")

for i, email in enumerate(emails, 1):
    score, risk, findings = analyze_email(
        email["subject"],
        email["sender"],
        email["body"],
        email["links"]
    )
    print_report(i, email["subject"], email["sender"], score, risk, findings)

print("\n[+] Full report saved: phishing_report.txt")