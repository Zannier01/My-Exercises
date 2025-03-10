print("Welcome to the quiz.") 
points = 0
playing = input("Do you want to play the game? ")

if playing != "yes":
    quit()

print("Okay, we're playing! ")
    
answer1 = input("What does CPU stand for? ")

if answer1 != ("Central Processing Unit" ):
    print("Incorrect answer.")
else:
    points+= 1


answer2 = input("What Porsche series was produced between 1994-1998? ")

if answer2 != ("993" ):
    print("Incorrect answer.")
else:
    points+= 1


print(points)