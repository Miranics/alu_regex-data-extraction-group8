import re

text = """
Call me at (123) 456-7890 or 123-456-7890.
You can also reach me at 123.456.7890 or 123 456 7890.
"""

phone_regex = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'

phone_numbers = re.findall(phone_regex, text)

print("Extracted phone numbers:", phone_numbers)

