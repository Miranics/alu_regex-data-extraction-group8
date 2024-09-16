import re

def extract_urls(text):
    """
    Extracts URLs from the given text using a regular expression.
    
    :param text: The input text containing URLs
    :return: A list of unique, valid URLs found in the text
    """
    # Improved regex pattern for URL extraction
    url_pattern = r'https?://(?:www\.)?[-\w]+(?:\.\w[-\w]*)+[\w\-._~:/?#[\]@!$&\'()*+,;=]*'
    urls = re.findall(url_pattern, text)

    # Remove duplicates
    unique_urls = list(set(urls))

    # Validate the domain portion of the URL
    valid_urls = [url for url in unique_urls if re.search(r'https?://[-\w]+\.\w{2,}', url)]

    return valid_urls

# Example usage
if __name__ == "__main__":
    sample_text = """
    Visit our website at https://www.example.com or follow us at http://subdomain.example.org/page.
    Check out our blog at https://blog.example.com/tech-news, or follow this invalid link: https://example...com.
    """
    
    # Extract URLs
    extracted_urls = extract_urls(sample_text)
    print("Extracted URLs:", extracted_urls)
