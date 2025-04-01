import re
def check_password_strength(password):
    # Initialize score
    score = 0
    feedback = []
    # Check length
    if len(password) < 8:
        feedback.append("Password is too short. It should be at least 8 characters.")
    else:
        score += 1
    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")
    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")
    # Check for digits
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add numbers.")
    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special characters.")
    # Evaluate score
    if score < 3:
        strength = "Weak"
    elif score < 5:
        strength = "Moderate"
    else:
        strength = "Strong"
    return strength, feedback
# Get password input
password = input("Enter a password: ")
# Check password strength
strength, feedback = check_password_strength(password)
# Print results
print(f"\nPassword strength: {strength}")
if feedback:
    print("Suggestions to improve:")
    for suggestion in feedback:
        print(f"- {suggestion}")
else:
    print("Great! Your password is strong.")