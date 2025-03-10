def prime_number_guesser(num):
    if num % 2 == 1:
        if num/num:
            print(f"Number {num} is a prime number.")
    else:
        print(f"Number {num} is NOT a prime number.")


user_input = int(input("Enter a Number: "))

prime_number_guesser(user_input)

#NOTICE: The function lacks a way to check for data type of the input.