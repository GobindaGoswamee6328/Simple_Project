
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
print("Starts the Football quiz")

guess1 = input("Who is the Most Complete Footballer in Football History?")
check_guess(guess1, "Cr7")

guess2 = input("Which country has won the most World Cups?")
check_guess(guess2, "Brazil")

guess3 = input("Which Team has more UCL titles?")
check_guess(guess3, "Real Madrid")

guess4 = input("Which country won the first ever World Cup in 1930?")
check_guess(guess4, "Uruguay")

guess5 = input("Which team won the first Premier League Title?")
check_guess(guess5, "Manchester United")

guess6 = input("Who is the Champions League's top goalscorer of all time?")
check_guess(guess6, "Cr7")

guess7 = input("Which is the best attacking trio in football history?")
check_guess(guess7, "MSN")

guess8 = input("Who is the best Free kick goal scorer of all time?")
check_guess(guess8, "Juninho")

guess9 = input("How many trophies Ramos have?")
check_guess(guess9, "22")

guess10 = input("Which Trio is Called the Barmuda Triangle?")
check_guess(guess10, "MCK")

guess11 = input("Who is the king of Football?")
check_guess(guess11, "Pele")

guess12 = input("Who scored the most goals at the age of 21?")
check_guess(guess12, "R9")

guess13 = input("Who is the master dribbler?")
check_guess(guess13, "Ronaldinho")

guess14 = input("Who is the 3rd best Player is this Generation?")
check_guess(guess14, "Neymar")

guess15 = input("Who is the greatest coach of all time?")
check_guess(guess15, "Sir Alex Ferguson")

print("Your Score is "+ str(score))
