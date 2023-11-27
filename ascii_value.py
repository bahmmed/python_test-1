user_input = input("Enter a string: ")
def ascii_value_of_string(input_string):
    for char in input_string:
        ascii_value = ord(char)
        print(f"   {char}           {ascii_value}")
        

# Display characters and their ASCII values
ascii_value_of_string(user_input)