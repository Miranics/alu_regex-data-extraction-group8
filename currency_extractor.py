import re

# Sample input text with currency amounts
sample_text = """
Here are some currency amounts:
$19.99
$1,234.56
$100
$12,345
$9.99
"""

# Regular expression to match currency amounts
currency_regex = r'\$\d{1,3}(,\d{3})*(\.\d{2})?'

# Find all currency amounts in the sample text
currency_amounts = re.findall(currency_regex, sample_text)

# Print extracted currency amounts
for amount in currency_amounts:
    print(amount)
