"""
main.py
-------
Runs the Password Strength Checker in the terminal.

The password is typed in hidden (using getpass) and is never
printed, saved or sent anywhere.
"""

import getpass

from password_checker import check_password


def get_password():
    """Ask the user for a password without showing it on screen."""
    try:
        password = getpass.getpass("Enter a password to check: ")
    except Exception:
        # Some terminals (like some IDE consoles) can't hide input,
        # so we fall back to normal input.
        print("(Hidden input not available, your typing will be visible.)")
        password = input("Enter a password to check: ")
    return password


def tick(condition):
    """Return a tick or a cross depending on the condition."""
    if condition:
        return "[✓]"
    return "[✗]"


def show_results(results):
    """Print the results in a nice layout."""
    print()
    print("PASSWORD STRENGTH CHECKER")
    print("=" * 30)
    print()
    print("Password Length:", results["length"])
    print()

    length_checks = results["length_checks"]
    print(tick(length_checks["min"]), "Minimum length reached (8)")
    print(tick(length_checks["good"]), "12 or more characters")
    print(tick(length_checks["great"]), "16 or more characters")
    print(tick(results["lowercase"]), "Contains lowercase letters")
    print(tick(results["uppercase"]), "Contains uppercase letters")
    print(tick(results["number"]), "Contains numbers")
    print(tick(results["special"]), "Contains special characters")
    print(tick(not results["common"]), "Not a common password")
    print()

    print("Score:", results["score"], "/ 8")
    print("Estimated Strength:", results["rating"].upper())
    print()

    print("Suggestions:")
    for suggestion in results["suggestions"]:
        print("-", suggestion)

    print()
    print("Note: This is a heuristic assessment, not a guarantee.")
    print("Long, unpredictable passwords matter more than ticking every box.")
    print()


def main():
    """Main loop of the program."""
    print("Welcome to the Password Strength Checker!")
    print("Your password is checked on your computer only. It is never saved.")
    print()

    keep_going = True

    while keep_going:
        password = get_password()

        # Stop empty passwords
        if password == "":
            print("You did not enter anything. Please try again.")
            print()
            continue

        results = check_password(password)
        show_results(results)

        answer = input("Check another password? (y/n): ").strip().lower()
        if answer != "y":
            keep_going = False
        print()

    print("Thanks for using the Password Strength Checker. Goodbye!")


if __name__ == "__main__":
    main()
