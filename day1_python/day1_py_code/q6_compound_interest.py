#6. Calculate the compound interest for a given principal amount, interest rate, and time period.

def calculate_compound_interest(principal, rate, time, n):
    # Formula for compound interest
    amount = principal * (1 + rate / (n * 100))**(n * time)
    compound_interest = amount - principal
    return compound_interest, amount

# Example usage
principal = 1000  # Initial principal amount
rate = 5  # Annual interest rate in percentage
time = 3  # Time period in years
n = 4  # Number of times interest applied per time period (quarterly)

compound_interest, total_amount = calculate_compound_interest(principal, rate, time, n)

print(f"Compound Interest: {compound_interest:.2f}")
print(f"Total Amount: {total_amount:.2f}")
