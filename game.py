from capitals import states
# from test_capitals import test_states
import random
# print(test_states)

play = True
while play == True:
    random.shuffle(states)

    print("\n Welcome to 'Learn Your State Capitals! When each state is shown, write the capital that matches. \n")
    print("******************************* \n")
    print("Please guess the capital: ")

# Set counters to 0
    correct = 0
    incorrect = 0
    round = len(states)
    # print(correct, incorrect, round)

    for i in states:
        print("States Remaining", round)
        print("----------------------------")
        print("State: " + i["name"],"\n")
        guess_capital = input("Capital: \n").lower()
        guess_capital = guess_capital.casefold()
        guess = i["capital"].casefold()
        guess.casefold() == guess_capital.casefold()
       
        if guess == guess_capital:
            correct+=1
            round-=1
            print("Correct!!")
            print("# Correct:", correct, "# Incorrect", incorrect)
        elif guess != guess_capital:
            incorrect+=1
            round-=1
            print("Incorrect.")
            print("Incorrect: ", i["capital"])
            print("# Correct:", correct, "# Incorrect", incorrect, "\n")
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
    
    





