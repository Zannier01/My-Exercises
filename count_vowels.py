vowels = ['a','e','i','o','u','y']


def check_vowels (word):
    vowels_in_word = []
    vowels_counter = 0
    for i in word:
        for j in vowels:
            if i == j:
                vowels_in_word.append(i)
                vowels_counter += 1
    print(f"The number of vowels is {vowels_counter} and the vowels are ({vowels_in_word})")    


print("Please enter a word.")
user_input = input()
check_vowels(user_input)
