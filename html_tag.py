import re

{ 'a', 'abbr', 'address', 'area', 'article', 'aside', 'audio', 'b', 'base', 'bdi',
    'bdo', 'blockquote', 'body', 'br', 'button', 'canvas', 'caption', 'cite', 'code',
    'col', 'colgroup', 'data', 'datalist', 'dd', 'del', 'details', 'dfn', 'dialog',
    'div', 'dl', 'dt', 'em', 'embed', 'fieldset', 'figcaption', 'figure', 'footer',
    'form', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'head', 'header', 'hgroup', 'hr',
    'html', 'i', 'iframe', 'img', 'input', 'ins', 'kbd', 'label', 'legend', 'li',
    'link', 'main', 'map', 'mark', 'meta', 'meter', 'nav', 'noscript', 'object',
    'ol', 'optgroup', 'option', 'output', 'p', 'picture', 'pre', 'progress', 'q',
    'rp', 'rt', 'ruby', 's', 'samp', 'script', 'section', 'select', 'small', 'source',
    'span', 'strong', 'style', 'sub', 'summary', 'sup', 'table', 'tbody', 'td', 'template',
    'textarea', 'tfoot', 'th', 'thead', 'time', 'title', 'tr', 'u', 'ul', 'var', 'video',
    'wbr'
}

def is_valid_html_tag(tag):
   
    tag_name_pattern = re.compile(r'^<(/?\s*([\w-]+))[^>]*>$')
    match = tag_name_pattern.match(tag)
    if match:
        tag_name = match.group(2).lower()  
        return tag_name in is_valid_html_tags
    else:
        return False

def main():
   
    html_string = input("Please Enter your HTML string:\n")

    
    html_tag_pattern = r'<[^>]+>'
    
   
    matches = re.findall(html_tag_pattern, html_string)
    
    if matches:
        print(" You got it!...valid html tag:")
        for match in matches:
            print(match)
    else:
        print("Oh No!... invalid html tag.")
        
while True:
    
    html_str = input("Enter an html tag (or type 'exit' to quit): ").strip()
    
    
    if html_str.lower() == 'exit':
        break

if __name__ == "__main__":
    main()





