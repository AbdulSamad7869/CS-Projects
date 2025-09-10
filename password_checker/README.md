# 🔒 Password Strength & Breach Checker

This Python script helps users choose **secure passwords** by checking both their **strength** (entropy & length) and whether they have been **exposed in known data breaches** using the [Have I Been Pwned API](https://haveibeenpwned.com/Passwords).

---

## 🚀 Features

- ✅ **Password Strength Evaluation**  
  - Uses entropy calculation based on character diversity (lowercase, uppercase, digits, symbols).  
  - Classifies passwords as:  
    - **Too Short ❌**  
    - **Weak ❌**  
    - **Medium ⚠️**  
    - **Strong ✅**

- ✅ **Data Breach Check**  
  - Uses SHA-1 hashing and the **k-anonymity model** to securely query the Have I Been Pwned API.  
  - Alerts users if their password has appeared in known breaches.  

- ✅ **Interactive CLI**  
  - Prompts users until they provide a safe password.  

---

## 📦 Installation

Clone the repository and install the only dependency:

```bash
git clone https://github.com/yourusername/password-checker.git
cd password-checker
pip install requests
```

---

## ⚡ Usage

Run the script:

```bash
python3 password_checker.py
```

Example Interaction:

```bash
Enter a password: 123456
❌ Password too short! Must be at least 8 characters.

Enter a password: qwertyuiop
❌ Password is too weak. Please try again.

Enter a password: Myp@ssw0rd2025!
Strength: Strong ✅
✅ This password has not been found in breaches.

```

---

## 🔍 How it works

1. Strength Check
- Minimum length: 8 characters
- Auto strong if: ≥16 characters or entropy ≥ 80 bits
- High randomness (≥35 bits) also counts as Strong
- Moderate entropy (≥50 bits) = Medium
2. Breach Check
- Password is hashed with SHA-1.
- First 5 characters of the hash are sent to Have I Been Pwned.
- Remaining hash is compared locally to preserve privacy.

  ---
