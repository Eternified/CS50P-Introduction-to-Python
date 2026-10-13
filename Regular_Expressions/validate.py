import re

email = input("What's your email? ").strip()

if re.fullmatch(r"(\w|\.)+@(\w+\.)*\w+\.(com|edu|gov|net|org|aol)", email, flags=re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
