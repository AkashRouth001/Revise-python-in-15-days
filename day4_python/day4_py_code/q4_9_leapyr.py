#9. Implement a function to check if a given year is a leap year or not.
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False

# Example usage
year = 2024
print(f"{year} is a leap year?" , is_leap_year(year))
