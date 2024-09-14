import re

def extract_emails(text):
        # Define the regular expression for matching email addresses
            email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
                
                    # Use re.findall() to find all email addresses in the text
                        emails = re.findall(email_pattern, text)
                            
                                return emails

