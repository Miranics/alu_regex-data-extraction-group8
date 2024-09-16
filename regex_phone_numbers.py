import re

text = """
Call me at (123) 456-7890 or 123-456-7890.
You can also reach me at 123.456.7890 or 123 456 7890.
"""

# Regular expression to match different phone number formats
phone_regex = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'

# Loop to allow user to input the phone number or exit
while True:
    # Ask the user to input a phone number or 'exit' to quit
    user_input = input("Enter the phone number you're looking for (or type 'exit' to quit): ").strip()
    
    if user_input.lower() == 'exit':
        print("Exiting...")
        break
    
    # Search for the phone number in the text
    phone_numbers = re.findall(phone_regex, text)
    
    # Check if the input matches any extracted phone numbers
    if user_input in phone_numbers:
        print(f"Phone number {user_input} found in the text!")
    else:
        print(f"Phone number {user_input} not found in the text.")
    
    # Display all extracted phone numbers
    print("Extracted phone numbers:", phone_numbers)
