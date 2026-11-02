"""
password_checker.py
-------------------
Contains the logic for the Password Strength Checker.

This is a simple, rule-based checker made for learning purposes.
It does NOT save or send passwords anywhere. Everything stays on
the user's computer.
"""

import string

# A small sample list of common passwords (just for learning).
# A real checker would use a much bigger list.
COMMON_PASSWORDS = [
    "password",
    "password1",
    "password123",
    "123456",
    "12345678",
    "123456789",
    "qwerty",
    "qwerty123",
    "abc123",
    "letmein",
    "welcome",
    "admin",
    "iloveyou",
    "monkey",
    "dragon",
    "football",
    "hello123",
    "11111111",
    "sunshine",
    "princess",
]

MIN_LENGTH = 8
GOOD_LENGTH = 12
GREAT_LENGTH = 16


# ---------- Character checking functions ----------

def has_lowercase(password):
    """Return True if the password has at least one lowercase letter."""
    for character in password:
        if character in string.ascii_lowercase:
            return True
    return False


def has_uppercase(password):
    """Return True if the password has at least one uppercase letter."""
    for character in password:
        if character in string.ascii_uppercase:
            return True
    return False


def has_number(password):
    """Return True if the password has at least one digit."""
    for character in password:
        if character in string.digits:
            return True
    return False


def has_special(password):
    """Return True if the password has at least one symbol like ! or @."""
    for character in password:
        if character in string.punctuation:
            return True
    return False


# ---------- Length checking functions ----------

def check_length(password):
    """Return a dictionary showing which length targets were reached."""
    length = len(password)
    results = {
        "min": length >= MIN_LENGTH,
        "good": length >= GOOD_LENGTH,
        "great": length >= GREAT_LENGTH,
    }
    return results


# ---------- Common password check ----------

def is_common_password(password):
    """Return True if the password is in the sample common password list."""
    # lower() so that "PASSWORD" is also caught
    if password.lower() in COMMON_PASSWORDS:
        return True
    return False


# ---------- Scoring ----------

def calculate_score(password):
    """
    Work out the score (0 to 8) using the rules in docs/PASSWORD-RULES.md.
    Each rule that is met gives +1 point.
    """
    score = 0

    length_results = check_length(password)
    if length_results["min"]:
        score += 1
    if length_results["good"]:
        score += 1
    if length_results["great"]:
        score += 1

    if has_lowercase(password):
        score += 1
    if has_uppercase(password):
        score += 1
    if has_number(password):
        score += 1
    if has_special(password):
        score += 1

    if not is_common_password(password):
        score += 1

    return score


def get_rating(score, common):
    """Turn a score into a rating word."""
    # A common password is always weak, whatever the score is
    if common:
        return "Weak"

    if score <= 3:
        return "Weak"
    elif score <= 5:
        return "Moderate"
    elif score <= 7:
        return "Strong"
    else:
        return "Very Strong"


# ---------- Suggestions ----------

def get_suggestions(password):
    """Return a list of tips to help improve the password."""
    suggestions = []
    length_results = check_length(password)

    if is_common_password(password):
        suggestions.append("This is a very common password. Do not use it.")

    if not length_results["min"]:
        suggestions.append("Increase password length (at least 8 characters).")
    if not length_results["good"]:
        suggestions.append("Consider using a longer passphrase (12+ characters).")

    if not has_lowercase(password):
        suggestions.append("Add some lowercase letters.")
    if not has_uppercase(password):
        suggestions.append("Add some uppercase letters.")
    if not has_number(password):
        suggestions.append("Add some numbers.")
    if not has_special(password):
        suggestions.append("Add some special characters (like ! or @).")

    # Always remind about predictable patterns
    suggestions.append("Avoid predictable password patterns.")

    return suggestions


# ---------- Main function that puts everything together ----------

def check_password(password):
    """
    Run all the checks and return the results in one dictionary,
    so main.py can just print them.
    """
    common = is_common_password(password)
    score = calculate_score(password)

    results = {
        "length": len(password),
        "length_checks": check_length(password),
        "lowercase": has_lowercase(password),
        "uppercase": has_uppercase(password),
        "number": has_number(password),
        "special": has_special(password),
        "common": common,
        "score": score,
        "rating": get_rating(score, common),
        "suggestions": get_suggestions(password),
    }
    return results
