import re

def extract_urls(text):
    """
    Extracts URLs from the given text using a regular expression.
    """
    url_pattern = r'https?://(?:www\.)?[-\w]+(?:\.\w[-\w]*)+[\w\-._~:/?#[\]@!$&\'()*+,;=]*'
    urls = re.findall(url_pattern, text)

    return list(set(urls))  # Remove duplicates

def process_urls():
    """
    Prompts the user for input and extracts URLs from the provided text.
    """
    try:
        text = input("Please enter the text for URL extraction:\n")
        
        if not text.strip():
            print("No text provided. Exiting.")
            return
        
        extracted_urls = extract_urls(text)
        
        if extracted_urls:
            print("\nExtracted URLs:")
            for url in extracted_urls:
                print(f"- {url}")
        else:
            print("No valid URLs found.")
    
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    process_urls()
