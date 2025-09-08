# 🔐 Password Checker

A Python tool that evaluates password strength and checks whether a password has been exposed in known data breaches using the [Have I Been Pwned](https://haveibeenpwned.com/API/v3) API.

## 📌 Features
- **Entropy Estimation** – Calculates password entropy (measure of randomness/complexity).  
- **Strength Classification** – Labels a password as **Too Short ❌**, **Weak ❌**, **Medium ⚠️**, or **Strong ✅**.  
- **Breach Check** – Uses the Have I Been Pwned API (k-anonymity model) to verify if the password has appeared in real-world data breaches.  
- **Interactive CLI** – Runs in a loop until a secure, unbreached password is entered.  

## ⚙️ Requirements
- Python 3.7+  
- `requests` library  

Install dependencies with:
```bash
pip install requests
