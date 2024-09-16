import re


html_string = """
<div class="container">
    <p>hi, Modestine!</p>
    <img src="image.jpg" alt="A beautiful image">
    <a href="https://example.com">Click here</a>
</div>
"""

html_tag_pattern = r"<[^>]+>"


matches = re.findall(html_tag_pattern, html_string)

def is_valid_html_tag(TAG):
    if TAG.startswith("<") and TAG.endswith(">"):
    
       return True
    else:
        return False


for match in matches:
    if is_valid_html_tag(match):
        print(f"{match} - valid html tag")
    else:
        print(f"{match} - invalid html tag")

for match in matches:
    print(match)

