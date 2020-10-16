from capitals import states
# from test_capitals import test_states
import random
# print(test_states)

play = True
while play == True:
    random.shuffle(states)

    print("Welcome to 'Learn Your State Capitals! When each state is shown, write the capital that matches")

    print("Please guess the capital: ")

# Set counters to 0
    correct = 0
    incorrect = 0
    round = len(states)
    # print(correct, incorrect, round)

    for i in states:
        print("States Remaining", round)
        print("----------------------------")
        print("State: " + i["name"])
        guess_capital = input("Guess the Capital: \n")
        guess = i["capital"].lower()
        guess.lower() == guess_capital.lower()
        if guess == guess_capital:
            correct+=1
            round-=1
            print(round, correct)
            print("Correct")
            print("# Correct:", correct, "# Incorrect", incorrect)
        elif guess != guess_capital:
            incorrect+=1
            round-=1
            print(round,incorrect)
            print("Incorrect: ", i["capital"])
            print("# Correct:", correct, "# Incorrect", incorrect)
        if round == 0:
            print("The game is over", correct, incorrect)
            print("Total Score:", correct+incorrect)
            print("Do you want to play again?")
    play_again = input("Please type yes or no: ")
    if play_again == "yes":
        play == True
        continue
    elif play_again == "no":
        play == False
        print("Goodbye")
        break
else: 
    play == False
    
    





