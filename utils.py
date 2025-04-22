import re


def normalize(text):
    return re.sub(r'[^a-z0-9]', '', text.lower())


def is_palindrome(text):
    cleaned = normalize(text)
    return cleaned == cleaned[::-1]
