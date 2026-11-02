# Password Rules

This file explains how the Password Strength Checker scores a password.
These are deliberately simple, educational rules.

## Scoring (0 to 8)

| Condition                              | Points |
|----------------------------------------|--------|
| At least 8 characters                  | +1     |
| At least 12 characters                 | +1     |
| At least 16 characters                 | +1     |
| Contains lowercase letters             | +1     |
| Contains uppercase letters             | +1     |
| Contains numbers                       | +1     |
| Contains special characters            | +1     |
| Not in the sample common-password list | +1     |

## Ratings

| Score | Rating      |
|-------|-------------|
| 0-3   | Weak        |
| 4-5   | Moderate    |
| 6-7   | Strong      |
| 8     | Very Strong |

A password found in the common-password list is **always rated Weak**,
whatever its score is.

## Limitations

- The common-password list is a small sample of 20 entries, not a real database.
- The checker does not detect keyboard patterns (like `qwertyuiop`), repeated
  characters, dates or names.
- A long, unpredictable passphrase is usually better than a short password that
  ticks every character category.
- This is a heuristic assessment, not a guarantee that a password is secure!!.

## Privacy

Passwords are checked locally. They are never printed, saved, logged or sent
anywhere. Never use real passwords in tests, screenshots or commits.
