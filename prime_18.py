def check_prime(num):
    """Check if a number is prime."""
    # Handle edge cases
    if num < 2:
        return False

    for data in range(2, num):
        if num % data == 0:
            return False

    return True
