def check_palindrome(word):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    cleaned_word = ''.join(word.split()).lower()
    # Check if the cleaned word is equal to its reverse
    return cleaned_word == cleaned_word[::-1]

# Take user input
user_word = input("Enter a word: ")

# Check if the word is a palindrome and display the result
if check_palindrome(user_word):
    print(f"{user_word} is a palindrome!")
else:
    print(f"{user_word} is not a palindrome.")
