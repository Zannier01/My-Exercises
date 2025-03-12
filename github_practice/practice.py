import random
def practice(number):
    for i in range(number+1):
        print(i)

# New Function to test commiting to new branch
def random_function():
    num1 = random.randint(10,10000)
    print(num1)

def add_numbers(a, b):
    return a + b


def user_name():
    name = input("Please state your name: ")
    print(name)

practice(9999)
result = add_numbers(3, 5)
print("Sum:", result)
random_function()

