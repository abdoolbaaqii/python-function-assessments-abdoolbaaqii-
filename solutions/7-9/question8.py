def is_armstrong(n):
    # Convert the number to string to get each digit
    digits = str(n)
    n_digits = len(digits)
    
    # Calculate the sum of each digit raised to the power of n_digits
    total = 0
    for digit in digits:
        total += int(digit) ** n_digits
    
    # Check if the sum is equal to the original number
    return total == n

# Test for numbers
print(is_armstrong(153))  # Output = True
print(is_armstrong(351))  # Output = False
print(is_armstrong(513))  # Output = False