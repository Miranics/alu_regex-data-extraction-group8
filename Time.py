import re


time_24hr_pattern = r'^(?:[01]\d|2[0-3]):[0-5]\d$'  
time_12hr_pattern = r'^(?:0?[1-9]|1[0-2]):[0-5]\d\s?[AaPp][Mm]$'  

# Additional logic to handle edge cases in the 12-hour format
def is_valid_12hr_format(time_str):
    match = re.fullmatch(time_12hr_pattern, time_str)
    if match:
        # Split time into parts
        time, meridiem = time_str[:-2].strip(), time_str[-2:].upper().strip()
        hour, minute = map(int, time.split(':'))

        # Ensure minutes are in a valid range (00-59)
        if not (0 <= minute < 60):
            return False

        # Special handling for 12 AM and 12 PM
        if meridiem == 'AM' and hour == 12:
            return True  
        elif meridiem == 'PM' and hour == 12:
            return True  

        # Validate hour (01-11 for AM/PM)
        if 1 <= hour <= 11:
            return True
    return False

# Function to identify time format with strict validation
def identify_time_format(time_str):
    if re.fullmatch(time_24hr_pattern, time_str):
        return "24-hour time format"
    elif is_valid_12hr_format(time_str):
        return "12-hour time format"
    else:
        return "Invalid time format"

# Main loop to take input from the terminal
while True:
    # Prompt the user for input
    time_str = input("Enter a time (or type 'exit' to quit): ").strip()
    
    # Exit condition
    if time_str.lower() == 'exit':
        break
    
    # Identify the time format
    result = identify_time_format(time_str)
    
    # Print the result
    print(f"'{time_str}' is in {result}")
