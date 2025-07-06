def time_converter(seconds):
    # First, calculate hours
    hours = seconds // 3600

    # Then calculate remaining seconds after taking out hours
    remaining_seconds = seconds % 3600

    # From the remaining seconds, calculate minutes
    minutes = remaining_seconds // 60


    secs = remaining_seconds % 60

    # Format as HH:MM:SS with leading zeros
    time = f"{hours:02d}:{minutes:02d}:{secs:02d}"
    return time

# Test case
print(time_converter(3661))  # Expected output: 01:01:01