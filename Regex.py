import re

print("\n=== REGEX DEMO ===")

# 1. Basic Search
text = "The cat sat on the mat."
pattern = r"cat"
match = re.search(pattern, text)
print(f"1. Basic Search for 'cat': Found at position {match.span() if match else 'Not Found'} -> '{match.group() if match else ''}'")

# 2. Character Classes and Quantifiers
text = "Contact: john.doe123@gmail.com or jane_smith@university.edu"
email_pattern = r"[\w._%+-]+@[\w.-]+\.[A-Za-z]{2,}"
emails = re.findall(email_pattern, text)
print(f"2. Found Emails: {emails}")

# 3. Extracting Phone Numbers
text = "Call me at 123-456-7890 or 987-654-3210 tomorrow."
phone_pattern = r"\d{3}-\d{3}-\d{4}"
phones = re.findall(phone_pattern, text)
print(f"3. Found Phone Numbers: {phones}")

# 4. Using Groups
text = "I have a red car and a blue bike."
pattern = r"(red|blue)\s+(car|bike)"
matches = re.findall(pattern, text)
print(f"4. Found Color-Object Pairs: {matches}")

# 5. Substitution (Cleaning Text)
text = "This    sentence  has   irregular    spacing."
cleaned = re.sub(r"\s+", " ", text) # Replace multiple spaces with single space
print(f"5. Cleaned Text: '{cleaned.strip()}'")

# 6. Splitting with Regex
text = "apple, orange; banana|grape"
fruits = re.split(r"[,;|]", text) # Split on comma, semicolon, or pipe
fruits = [fruit.strip() for fruit in fruits] # Clean whitespace
print(f"6. Split Fruits: {fruits}")

# 7. Validation with Anchors
def is_valid_username(username):
    """Validates a username (3-16 chars, letters/numbers/underscore)."""
    pattern = r"^[a-zA-Z0-9_]{3,16}$"
    return bool(re.match(pattern, username))

usernames = ["user_1", "a", "this_username_is_too_long", "valid123"]
print("7. Username Validation:")
for name in usernames:
    print(f"   '{name}' -> {'Valid' if is_valid_username(name) else 'Invalid'}")
