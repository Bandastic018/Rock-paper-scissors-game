from pickle import FALSE
import random

print("<Welcome to Rock-Paper-Scissors Game>")
while True:

    out_come = ["R", "P", "S"]

    player = input(
        "Pick between R for Rock, P for Paper and S for Scissors:", ).upper()
    player_input = ""

    Computer_input = ""

    while player not in out_come:
        print("Error!, Your entry is wrong. Please try again.")
        player = input(
            "Pick between R for Rock, P for Paper and S for Scissors:", ).upper()

    if player == "R":
        player_input = "Rock"
    elif player == "S":
        player_input = "Scissors"
    elif player == "P":
        player_input = "Paper"

    print("Player:", player)

    Computer = random.choice(out_come)
    print("CPU player:", Computer)

    if Computer == "R":
        Computer_input = "Rock"
    elif Computer == "S":
        Computer_input = "Scissors"
    elif Computer == "P":
        Computer_input = "Paper"

    print(f'Player ({player_input}) : CPU ({Computer_input})')

    if player_input == "Rock":
        if Computer_input == "Scissors":
            print("Hurrayyy!!!, You win!!!")
        elif Computer_input == "Paper":
            print("Hurraay!!!, CPU player wins!!!")

    if player_input == "Paper":
        if Computer_input == "Scissors":
            print("Hurrayyy!!!, CPU player wins!!!")
        elif Computer_input == "Rock":
            print("Hurray.!!!, You win!!!")

    if player_input == "Scissors":
        if Computer_input == "Rock":
            print("Hurrayyy!!!, CPU player wins!!!")
        elif Computer_input == "Paper":
            print("Hurray.!!!, You win!!!")

    if player_input == Computer_input:
        print("It's a tie!!!. Try again.")
    elif FALSE:
        break
print("Bye Bye!!!, Have a nice day!")
