def anagram_checker(word1, word2):
    if len(word1) != len(word2):
        print("Words are not the same length, therefore can't be anagrams")
        return
    else:
         res1 = "".join(sorted(word1.lower()))
         res2 = "".join(sorted(word2.lower()))
         if res1 != res2:
             print(f"The words {word1} and {word2} are NOT anagrams.")
         elif res1 == res2:
             print(f"The words {word1} and {word2} are anagrams.") 

user_input1 = str(input("Enter your first word: "))
user_input2 = str(input("Enter your second word: "))

anagram_checker(user_input1,user_input2)

#Program lacks exception for different data structures entered as input. Program can handle case sensitivity and
#excludes anything that is not the same length.

