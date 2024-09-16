import re


patterns = {
    'email': r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
    'url': r'https?://(?:www\.)?[-\w]+(?:\.\w[-\w])+[\w\-._~:/?#[\]@!$&\'()+,;=]*',
    'phone': r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',
    'credit_card': r'\b(?:\d{4}[-\s]){3}\d{4}\b|\b\d{4}[-\s]\d{6}[-\s]\d{5}\b|\b\d{4}[-\s]{3,6}\d{4}\b',
    'time': r'\b(?:[01]\d|2[0-3]):[0-5]\d\b|\b(?:[1-9]|1[0-2]):[0-5]\d\s?[APM]{2}\b',
    'html_tag': r'<[^>]+>',
    'hashtag': r'#\w+',
    'currency': r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
}


def luhn_algorithm(card_number):
    card_number = card_number.replace(" ", "").replace("-", "")
    total = 0
    reverse_digits = card_number[::-1]
    for i, digit in enumerate(reverse_digits):
        n = int(digit)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n
    return total % 10 == 0


def is_valid_card_prefix(card_number):
    card_number = card_number.replace(" ", "").replace("-", "")
    valid_prefixes = {
        "Visa": r'^4\d{12}(?:\d{3})?$',
        "MasterCard": r'^5[1-5]\d{14}$',
        "American Express": r'^3[47]\d{13}$',
        "Discover": r'^6(?:011|5\d{2})\d{12}$',
        "JCB": r'^(?:2131|1800|35\d{3})\d{11}$',
        "Diners Club": r'^3(?:0[0-5]|[68]\d)\d{11}$',
        "Maestro": r'^(?:5[0678]\d{2}|6304|6390|67\d{2})\d{8,15}$'
    }
    for card_type, prefix_pattern in valid_prefixes.items():
        if re.match(prefix_pattern, card_number):
            return True, card_type
    return False, None


def find_and_validate_credit_card_numbers(text):
    potential_cards = re.findall(patterns['credit_card'], text)
    valid_cards = []
    for card in potential_cards:
        normalized_card = card.replace(" ", "").replace("-", "")
        if luhn_algorithm(normalized_card):
            is_valid, card_type = is_valid_card_prefix(normalized_card)
            if is_valid:
                valid_cards.append((card, card_type))
    return valid_cards


def extract_data(text, data_type):
    pattern = patterns.get(data_type)
    if not pattern:
        raise ValueError(f"Unknown data type: {data_type}")
    return re.findall(pattern, text)

def print_welcome_message():
    print("Welcome to the Data Extraction Tool!")
    print("This tool can extract various types of data from your text input.")
    print("You can extract emails, URLs, phone numbers, credit card numbers, HTML tags, hashtags, currency amounts, and time formats.")
    print("Choose an option from the menu below.")

def print_menu():
    print("\nMenu:")
    print("1. Extract Emails")
    print("2. Extract URLs")
    print("3. Extract Phone Numbers")
    print("4. Extract Credit Card Numbers")
    print("5. Extract HTML Tags")
    print("6. Extract Hashtags")
    print("7. Extract Currency Amounts")
    print("8. Extract Time Formats")
    print("9. Exit")

def main():
    print_welcome_message()
    
    while True:
        print_menu()
        choice = input("\nEnter the number of your choice: ").strip()

        if choice == '9':
            print("Exiting the tool. Have a great day!")
            break

        if choice not in ['1', '2', '3', '4', '5', '6', '7', '8']:
            print("Invalid choice. Please select a valid option from the menu.")
            continue

        text_input = input("Enter your text string:\n")

        if choice == '1':
            data_type = 'email'
        elif choice == '2':
            data_type = 'url'
        elif choice == '3':
            data_type = 'phone'
        elif choice == '4':
            data_type = 'credit_card'
            valid_credit_card_numbers = find_and_validate_credit_card_numbers(text_input)
            if valid_credit_card_numbers:
                for card, card_type in valid_credit_card_numbers:
                    print(f"Valid {card_type} credit card found: {card}")
            else:
                print("No valid credit card numbers found.")
            continue
        elif choice == '5':
            data_type = 'html_tag'
        elif choice == '6':
            data_type = 'hashtag'
        elif choice == '7':
            data_type = 'currency'
        elif choice == '8':
            data_type = 'time'

        matches = extract_data(text_input, data_type)

        if matches:
            print(f"\n{data_type.capitalize()} extracted:")
            for match in matches:
                print(match)
        else:
            print(f"Sorry! No {data_type} found.")

if __name__ == "__main__":
    main()
