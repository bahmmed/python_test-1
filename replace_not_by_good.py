def replace_not_with_good(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Iterate through the words and replace "not" with "good"
    modified_words = [word if word.lower() != "not" else "good" for word in words]

    # Join the modified words to form the modified sentence
    modified_sentence = ' '.join(modified_words)

    return modified_sentence

# Take user input
user_sentence = input("Enter a sentence: ")

# Replace "not" with "good" in the sentence
modified_sentence = replace_not_with_good(user_sentence)

# Display the modified sentence
print("Modified Sentence:", modified_sentence)
