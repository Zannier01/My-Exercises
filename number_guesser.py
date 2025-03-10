import random

top_of_range = input ("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Write a number larger than 0. ")
        quit()
else:
    print("Write a number. ")
    quit()
randm_number = random.randint (0,top_of_range)
print(randm_number)



