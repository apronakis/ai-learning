# Create a function that takes a string representing a date and a pattern and converts it into a python datetime object 

from datetime import datetime

def string_to_datetime(date_string, pattern):
    """
    Convert a string representing a date into a Python datetime object.
    
    Args:
        date_string (str): The date as a string (e.g., "2026-06-01")
        pattern (str): The pattern to parse the date (e.g., "%Y-%m-%d")
    
    Returns:
        datetime: A datetime object representing the parsed date
    
    Raises:
        ValueError: If the date string does not match the pattern
    """
    return datetime.strptime(date_string, pattern)


# Example usage:
if __name__ == "__main__":
    # Example 1: ISO format date
    date_str_1 = "2026-06-01"
    pattern_1 = "%Y-%m-%d"
    result_1 = string_to_datetime(date_str_1, pattern_1)
    print(f"Input: {date_str_1} -> Output: {result_1}")
    
    # Example 2: US format date
    date_str_2 = "06/01/2026"
    pattern_2 = "%m/%d/%Y"
    result_2 = string_to_datetime(date_str_2, pattern_2)
    print(f"Input: {date_str_2} -> Output: {result_2}")
    
    # Example 3: Full datetime string
    date_str_3 = "2026-06-01 14:30:45"
    pattern_3 = "%Y-%m-%d %H:%M:%S"
    result_3 = string_to_datetime(date_str_3, pattern_3)
    print(f"Input: {date_str_3} -> Output: {result_3}")
