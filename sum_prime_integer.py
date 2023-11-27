def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def sum_of_primes(numbers):
    prime_numbers = [num for num in numbers if is_prime(num)]
    return sum(prime_numbers)

# Example: Take a list of integers as input
user_input = input("Enter a list of integers separated by spaces: ")
input_list = [int(num) for num in user_input.split()]

# Calculate the sum of prime numbers in the list
result = sum_of_primes(input_list)

# Display the result
print("Sum of Prime Numbers:", result)
