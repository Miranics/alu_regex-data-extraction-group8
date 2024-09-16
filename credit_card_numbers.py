import re

# Regular expression pattern for matching credit card numbers (space-separated or hyphen-separated)
credit_card_pattern = r'\b(?:\d{4}[-\s]){3}\d{4}\b|\b\d{4}[-\s]\d{6}[-\s]\d{5}\b|\b\d{4}[-\s]{3,6}\d{4}\b'

# Luhn's algorithm to check if a credit card number is valid
def luhn_algorithm(card_number):
    # Remove spaces and hyphens
    card_number = card_number.replace(" ", "").replace("-", "")
    
    # Reverse the card number and apply Luhn's algorithm
    total = 0
    reverse_digits = card_number[::-1]
    
    for i, digit in enumerate(reverse_digits):
        n = int(digit)
        # Double every second digit
        if i % 2 == 1:
            n *= 2
            # If doubling results in a number greater than 9, subtract 9
            if n > 9:
                n -= 9
        total += n

    # Valid if the total modulo 10 is 0
    return total % 10 == 0

# Function to check if the card has a valid prefix (Visa, MasterCard, etc.)
def is_valid_card_prefix(card_number):
    # Remove spaces and hyphens
    card_number = card_number.replace(" ", "").replace("-", "")
    
    # Check known prefixes
    valid_prefixes = {
        "Visa": r'^4\d{12}(?:\d{3})?$',                             # Visa cards
        "MasterCard": r'^5[1-5]\d{14}$',                           # MasterCard
        "American Express": r'^3[47]\d{13}$',                      # American Express (Amex)
        "Discover": r'^6(?:011|5\d{2})\d{12}$',                    # Discover
        "JCB": r'^(?:2131|1800|35\d{3})\d{11}$',                   # JCB
        "Diners Club": r'^3(?:0[0-5]|[68]\d)\d{11}$',              # Diners Club
        "Maestro": r'^(?:5[0678]\d{2}|6304|6390|67\d{2})\d{8,15}$' # Maestro (8-15 digits)
    }

    # Validate the card number against the known prefixes
    for card_type, prefix_pattern in valid_prefixes.items():
        if re.match(prefix_pattern, card_number):
            return True, card_type
    return False, None

# Function to find and validate credit card numbers in a given string
def find_and_validate_credit_card_numbers(text):
    potential_cards = re.findall(credit_card_pattern, text)
    valid_cards = []
    
    for card in potential_cards:
        # Remove spaces and hyphens for validation
        normalized_card = card.replace(" ", "").replace("-", "")
        
        if luhn_algorithm(normalized_card):
            is_valid, card_type = is_valid_card_prefix(normalized_card)
            if is_valid:
                valid_cards.append((card, card_type))
    
    return valid_cards

# Main function to take input from the terminal
if __name__ == "__main__":
    while True:
        # Take input string containing potential credit card numbers from the user
        sample_text = input("Enter the text containing credit card numbers (or type 'exit' to quit): ")
        
        # Exit condition
        if sample_text.lower() == 'exit':
            break
        
        # Find and print all valid credit card numbers
        valid_credit_card_numbers = find_and_validate_credit_card_numbers(sample_text)
        
        if valid_credit_card_numbers:
            for card, card_type in valid_credit_card_numbers:
                print(f"Valid {card_type} credit card found: {card}")
        else:
            print("No valid credit card numbers found.")
