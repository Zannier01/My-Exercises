def check_palindrome(word):

    if not isinstance(word,str):
        raise TypeError("Input must be a string/word.")
    

    reversed_word = word[::-1]
    if word == reversed_word:
        print(f"The word {word} is in fact a palindrome.")
    else:
        print(f"The word {word} is NOT in fact a palindrome.")



print("Enter a word and I will see if its a palindrome.")

try:
    user_input = input()
    check_palindrome(user_input)
except TypeError as e:
    print(f"Error: {e}")


