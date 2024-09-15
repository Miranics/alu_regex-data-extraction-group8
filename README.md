Regex Data Extraction Project
This project is part of the Regex Onboarding Hackathon and is aimed at demonstrating the use of Regular Expressions (Regex) to extract specific data types from unstructured text. The project handles various formats including email addresses, URLs, phone numbers, credit card numbers, and more, all through the power of Regex.
![download (1)](https://github.com/user-attachments/assets/e49e97fc-514f-4571-b513-7e6191144073)



Overview
In this project, we have implemented a series of Python scripts that extract important pieces of data from raw text. Whether it's web-scraped content or API responses, the scripts utilize regular expressions to efficiently find and extract the following data types:

Email Addresses
URLs
Phone Numbers
Credit Card Numbers
Time Formats (12-hour and 24-hour)
HTML Tags
Hashtags
Currency Amounts
Technologies Used
1. Python
Python was chosen as the primary programming language for this project due to its simplicity and support for powerful libraries. It helps us manage complex text processing tasks using concise code.

2. Regular Expressions (Regex)
Regex allows for precise pattern matching to extract data from unstructured strings. In this project, each type of data is extracted using specific regular expression patterns, ensuring accuracy in identifying emails, URLs, phone numbers, etc.

3. Python Libraries
re (Regular Expressions): The built-in re module in Python is used extensively for all pattern matching and data extraction tasks.
Unit Testing: Python’s unittest framework is used for testing the extraction functions to ensure they work correctly across various scenarios.
4. Version Control with GitHub
The project is managed and version-controlled using GitHub. Each team member contributed to a specific task, making use of branches and pull requests to collaboratively build the final solution.

Project Breakdown
Email Address Extraction
The email extractor uses a regular expression designed to match standard email formats such as:

user@example.com
firstname.lastname@company.co.uk
URL Extraction
The URL extractor captures various types of URLs, including:

https://www.example.com
http://subdomain.example.org/page
Phone Number Extraction
Various phone number formats are supported, such as:

(123) 456-7890
123-456-7890
123.456.7890
Credit Card Number Extraction
The system can identify common credit card formats like:

1234 5678 9012 3456
1234-5678-9012-3456
Currency Amount Extraction
Regular expressions capture different formats of currency:

$19.99
$1,234.56
How It Works
The process starts by feeding a large string or webpage data into the program. The text is parsed, and each type of information (e.g., emails, phone numbers) is extracted using specialized regular expressions. The extracted data can then be stored, displayed, or processed further.

Example Code for Email Extraction:
python
Copy code
import re

def extract_emails(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)
    return emails

# Example usage
sample_text = "Contact us at support@example.com or sales@company.co.uk."
emails = extract_emails(sample_text)
print("Extracted Emails:", emails)
Conclusion
This project showcases the effectiveness of regular expressions in extracting valuable information from vast, unstructured text sources. By utilizing Python and Regex, the team has built a robust solution for processing and extracting multiple types of data, essential for web scraping and data analysis tasks.

