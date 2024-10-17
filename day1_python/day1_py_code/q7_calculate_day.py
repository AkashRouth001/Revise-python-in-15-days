#7. Write a program that converts a given number of days into years, weeks, and days.

def convert_days(total_days):
    years = total_days // 365
    remaining_days = total_days % 365
    weeks = remaining_days // 7
    days = remaining_days % 7
    return years, weeks, days

# Example usage
total_days = 500
years, weeks, days = convert_days(total_days)

print(f"{total_days} days is equivalent to {years} years, {weeks} weeks, and {days} days.")
