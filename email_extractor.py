import re

# Read input file
with open("input.txt", "r", encoding="utf-8") as file:
    content = file.read()

# Extract email addresses
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", content)

# Save emails to output file
with open("emails.txt", "w", encoding="utf-8") as file:
    for email in emails:
        file.write(email + "\n")

print("Email addresses extracted successfully!")
print("Saved in emails.txt")