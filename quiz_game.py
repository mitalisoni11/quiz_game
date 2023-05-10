questions = {"What does CPU stand for?":"central processing unit",
             "What is the national capital of India?": "new delhi",
             "What does RAM stand for?":"random access memory"}
points = 0

print("Welcome to Quizzicle")

playing = input("Do you want to play? ")
if playing.lower() != "yes":
    print("Goodbye! See you againno")
    quit()

print("Let's play!")

for i in list(questions.keys()):
    Answer = input(i)
    if Answer.lower() == questions[i]:
        print("Correct!")
        points += 1
    else:
        print("Oops! That's incorrect")

print("Game Over! You earned {} points".format(points))


