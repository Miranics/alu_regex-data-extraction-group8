import re

def extract_urls(text):
    """
    Extracts URLs from the given text using a regular expression.
    
    :param text: The input text containing URLs
    :return: A list of URLs found in the text
    """
    url_pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
    urls = re.findall(url_pattern, text)
    return urls


# Example usage
if __name__ == "__main__":
    sample_text = """
    Visit our website at https://www.example.com or follow us on http://subdomain.example.org/page.
    You can also check https://example.net for more info.
    """
    extracted_urls = extract_urls(sample_text)
    print("Extracted URLs:", extracted_urls)
