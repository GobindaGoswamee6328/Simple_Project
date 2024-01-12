
def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry Wrong Answer, try again")
            attempt = attempt + 1
    if attempt == 3:
        print("The Correct answer is ",answer )

score = 0
print("Guess the Animal")
guess1 = input("What type of animal is a fer-de-lance?")
check_guess(guess1, "Snake")

guess2 = input("Which is the fastest land animal? ")
check_guess(guess2, "Cheetah")

guess3 = input("How many bones does a shark have?")
check_guess(guess3, "None")

guess4 = input("How many compartments does a cow’s stomach have?")
check_guess(guess4, "Four")

guess5 = input("Which animal has the largest eyes in the animal kingdom?")
check_guess(guess5, "The giant Squid")

print("Your Score is "+ str(score))
