import re

def extract_emails(text):
    """
    Extracts email addresses from the given text or list of text strings using a regular expression.
    """
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)

    return list(set(emails))  # Remove duplicates

def process_emails():
    """
    Prompts the user for input and extracts email addresses from the provided text.
    """
    try:
        text = input("Please enter the text for email extraction:\n")
        
        if not text.strip():
            print("No text provided. Exiting.")
            return
        
        extracted_emails = extract_emails(text)
        
        if extracted_emails:
            print("\nExtracted Emails:")
            for email in extracted_emails:
                print(f"- {email}")
        else:
            print("No valid email addresses found.")
    
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    process_emails()
