import re
import requests
import hashlib
import math

# Minimum length requirement for any password
MIN_LENGTH = 8
# Length at which a password is automatically considered strong
STRONG_LENGTH = 16


def password_entropy(password: str) -> float:
    """
    Estimate password entropy (in bits) based on character set size and length.
    Entropy is a measure of how hard a password is to brute-force.
    """
    charset = 0

    # Check which character groups are present and add their size to charset
    if re.search(r"[a-z]", password):
        charset += 26  # lowercase letters
    if re.search(r"[A-Z]", password):
        charset += 26  # uppercase letters
    if re.search(r"\d", password):
        charset += 10  # digits
    if re.search(r"\W", password):
        charset += 33  # printable symbols/punctuation

    # Fallback: if somehow none matched, assume lowercase only
    if charset == 0:
        charset = 26

    # Entropy formula: log2(possible_combinations)
    entropy = math.log2(charset ** len(password))
    return entropy


def check_strength(password: str) -> str:
    """
    Classify a password as Too Short, Weak, Medium, or Strong
    based on length and entropy estimation.
    """
    length = len(password)
    entropy = password_entropy(password)

    # Too short = reject immediately
    if length < MIN_LENGTH:
        return "Too Short ❌"

    # Very long or extremely high-entropy = always strong
    if length >= STRONG_LENGTH or entropy >= 80:
        return "Strong ✅"

    # Special case: 8+ characters with high randomness (entropy >= 35)
    if length >= MIN_LENGTH and entropy >= 35:
        return "Strong ✅"

    # Moderate entropy = medium
    if entropy >= 50:
        return "Medium ⚠️"

    # Anything else = weak
    return "Weak ❌"


def check_pwned(password: str) -> bool:
    """
    Check if the password appears in known data breaches
    using the Have I Been Pwned API (k-anonymity model).
    """
    # Hash the password using SHA1
    sha1_pw = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    prefix, suffix = sha1_pw[:5], sha1_pw[5:]

    # Query only the first 5 chars of the hash (privacy-preserving)
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    # If the suffix is in the results, the password was exposed
    return suffix in response.text


if __name__ == "__main__":
    while True:
        pw = input("Enter a password: ")

        # Run password strength checks
        strength = check_strength(pw)

        # Too short → reject immediately
        if strength == "Too Short ❌":
            print(f"❌ Password too short! Must be at least {MIN_LENGTH} characters.")
            continue

        # Weak passwords are not accepted
        if strength == "Weak ❌":
            print("❌ Password is too weak. Please try again.")
            continue

        # Check against known breaches
        if check_pwned(pw):
            print("⚠️ This password has been exposed in data breaches! Please choose another one.")
            continue

        # If we get here, password is Medium or Strong and not breached
        print("Strength:", strength)
        print("✅ This password has not been found in breaches.")
        break

