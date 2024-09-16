import re

def main():
  
    text_input = input("Enter your text string:\n")

   
    hashtag_pattern = r'#\w+'
    
    
    matches = re.findall(hashtag_pattern, text_input)
    
    
    if matches:
        print("Hashtags extracted:")
        for match in matches:
            print(match)
    else:
        print("No hashtags found.")
        

    

if __name__ == "__main__":
    main()
