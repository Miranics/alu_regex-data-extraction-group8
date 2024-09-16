import re

def extract_emails(text):
    """
    Extracts email addresses from the given text using a regular expression.
    
    :param text: The input text containing email addresses
    :return: A list of unique, valid email addresses found in the text
    """
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)

    # Remove duplicates
    unique_emails = list(set(emails))

    valid_emails = [email for email in unique_emails if re.search(r'@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', email)]

    return valid_emails

# Example usage
if __name__ == "__main__":
    sample_text = """
    Contact us at support@example.com or marketing@example.com. For more info, email miracle.nanen@company.co.uk.
    Or send your CV to hr@nonexistent..com or hr@fake@domain.com
    """
    
    # Extract emails
    extracted_emails = extract_emails(sample_text)
    print("Extracted Emails:", extracted_emails)
