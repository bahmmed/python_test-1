def check_alphabet(input_string):
    return input_string.isalpha()

# Take user input
user_input = input("Enter a string: ")

# Check if the input contains only alphabetical characters
if check_alphabet(user_input):
    # Print the string in uppercase
    uppercase_string = user_input.upper()
    print("Uppercase:", uppercase_string)
else:
    print("Error: Input should contain only alphabetical characters.")
