import string

def check_panagram(sentence):
    # Define the alphabet set
    alphabet_set = set(string.ascii_lowercase)
    
    # Clean and normalize the input
    sentence = sentence.replace(" ", "").lower()
    
    # Create a set of characters in the sentence
    sentence_set = set(char for char in sentence if char.isalpha())
    
    # Check if the sentence set contains all alphabet letters
    return sentence_set == alphabet_set


# User input
user_input = input("Enter a sentence: ")

# Check if it's a pangram
if check_panagram(user_input):
    print("This is a pangram!")
else:
    print("This is NOT a pangram.")
