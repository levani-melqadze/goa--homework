def shorten_date(date_string):
    return date_string.split(",")[0]

# Example usage
print(shorten_date("Friday May 2, 7pm"))  # Output: "Friday May 2"
