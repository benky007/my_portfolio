import random

playing = "on"
while playing == "on": 
    options = ["rock", "paper", "scissors"]
    your_score = 0
    winning_options = ["rockscissors", "paperrock", "scissorspaper"]
    losing_options = ["scissorsrock", "rockpaper", "paperscissors"]

    my_choice = input("your choice:")
    comp_choice = random.choice(options)
        
    choices = (comp_choice + my_choice)

    print("I chose ", comp_choice, " ", sep='', end='')
    '''
    if my_choice=="rock":
        if comp_choice=="rock":
            your_score + 0
            print("you drew")
            print("better luck next time, how about another game")
        elif comp_choice=="paper":
            your_score - 1
            print("you lost")
            print("good try, how about another game")
        elif comp_choice=="scissors":
            your_score + 1
            print("you won")
            print("you did really well, do you want another game")
    elif my_choice=="paper":
        if comp_choice=="rock":
            your_score + 1
            print("you won")
            print("you did really well, do you want another game")
        elif comp_choice=="paper":
            your_score + 0
            print("you drew")
            print("better luck next time, how about another game")
        elif comp_choice=="scissors":
            your_score - 1
            print("you lost")
            print("good try, how about another game")
    elif my_choice=="scissors":
        if comp_choice=="rock":
            your_score - 1
            print("you lost")
            print("good try, how about another game")
        elif comp_choice=="paper":
            your_score + 1
            print("you won")
            print("you did really well, do you want another game")
        elif comp_choice=="scissors":
            your_score + 0
            print("you drew")
            print("better luck next time, how about another game")
    elif my_choice=="bye":
        playing = "off"
    else:
        print("Learn to type properly and play again, ooft thot")
    '''

    if comp_choice==my_choice:
        your_score + 0
        print("you drew")
        print("better luck next time, how about another game")
    elif choices==winning_options:
        your_score + 1
        print("you won")
        print("you did really well, do you want another game")
    elif choices==losing_options:
        your_score - 1
        print("you lost")
        print("good try, do you want another game")
    elif my_choice=="bye":
        playing = "off"
        print("Bye bye then")
        print("your score is", " ", your_score, " ", sep='', end='')
        
    play_agian = input("do you want to play agian[y/n]: ")
    if play_agian=="n":
        print("Bye bye then")
        print("your score is", " ", your_score, " ", sep='', end='')
        playing = "off"
    elif play_agian=="y":
        print("Lets play again then")
    else:
        print("type an answer correctly next time")
