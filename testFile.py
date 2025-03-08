import re

def is_palindrome(s: str) -> bool:
    clean_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

    return clean_s == clean_s[::-1]

print(is_palindrome("racecar"))
print(is_palindrome("hello"))