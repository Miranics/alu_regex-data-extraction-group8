import re

# More accurate regular expressions
time_24hr_pattern = r'^(?:[01]\d|2[0-3]):[0-5]\d$'  # Strict 24-hour format (00:00 - 23:59)
time_12hr_pattern = r'^(?:0?[1-9]|1[0-2]):[0-5]\d\s?[APap][Mm]$'  # Strict 12-hour format (01:00 - 12:59 AM/PM)

# Function to identify time format
def identify_time_format(time_str):
    if re.fullmatch(time_24hr_pattern, time_str):
        return "24-hour time format"
    elif re.fullmatch(time_12hr_pattern, time_str):
        return "12-hour time format"
    else:
        return "Invalid time format"

# Sample times to test
time_samples = [
    "14:30",    # 24-hour format
    "02:30 PM", # 12-hour format (valid with leading 0)
    "09:45",    # 24-hour format
    "4:15 AM",  # 12-hour format (valid without leading 0)
    "25:00",    # Invalid time (hours exceed 24)
    "13:75",    # Invalid time (minutes exceed 59)
    "7:45 PM",  # 12-hour format
    "12:00 AM", # 12-hour format
    "00:00",    # Valid 24-hour format (midnight)
    "23:59",    # Valid 24-hour format (one minute to midnight)
    "11:59 PM", # Valid 12-hour format
    "13:00 PM", # Invalid time (hours exceed 12 for 12-hour format)
    "12:60 AM"  # Invalid time (minutes exceed 59)
]

# Check each time sample and identify its format
for time_str in time_samples:
    result = identify_time_format(time_str)
    print(f"'{time_str}' is in {result}")
