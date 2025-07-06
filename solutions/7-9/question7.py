# Function to calculate tax income
def calculate_tax(income):
    # First $10,000 is tax-free
    if income <= 10000:
        tax = 0
    # Next $10,000 is taxed at 10%
    elif income <= 20000:
        tax = (income - 10000) * 0.10
    # Any amount above $20,000 is taxed at 20%
    else:
        tax = (10000 * 0.10) + (income - 20000) * 0.20
    
    return tax

# Test for $15,000
income_1 = 15000
tax_1 = calculate_tax(income_1)
print("Tax for $15,000 income is:", tax_1)  # Output: 500

# Test for $30,000
income_2 = 30000
tax_2 = calculate_tax(income_2)
print("Tax for $30,000 income is:", tax_2)  # Output: 3000