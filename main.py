from turtle import Turtle, Screen
import random
from tkinter import messagebox as mb

# Setup Variables and Style
screen = Screen()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
is_race_on = False
screen.setup(width=500, height=400)
player_bets = {}
player_colors = []


def multi_player():
    """Takes user input and returns the number of players in a multiplayer game"""
    num_players = int(screen.textinput(title="Who's playing?", prompt="How many players are there? Between 2 and 6."))
    for j in range(1, num_players + 1):
        user_name = screen.textinput(title="Getting Info", prompt=f"Player {j}, what is your name?")
        user_bet = screen.textinput(title="Make Your Bet", prompt="Who will win the race? Enter a color.")
        player_bets[user_name] = user_bet
        player_colors.append(user_bet)
    return num_players


def single_player():
    """Takes user input and returns the users bet in a singleplayer game"""
    num_players = 6
    user_name = screen.textinput(title="Getting Info", prompt="Hello, what is your name?")
    user_bet = screen.textinput(title="Make Your Bet", prompt="Who will win the race? Enter a color.\n"
                                                              "Your choices are:\n'red', 'yellow', 'orange', 'green' ,"
                                                              "'blue', or 'purple'.")
    player_bets[user_name] = user_bet
    return user_bet


# User input setup
single_or_multi = screen.textinput(title="Welcome!", prompt="Single player (s) or Multiplayer (m)?").lower()
if single_or_multi == "m":
    players = multi_player()
else:
    single_bet = single_player()
    players = 6

# Set starting position for type of race
positions = [-15, -30, -45, -60, -70]
y = positions[players - 2]

# Create turtles for each player in the race
for turtle in range(players):
    new_turtle = Turtle(shape="turtle")
    if single_or_multi == "s":
        new_turtle.color(colors[turtle])
    else:
        new_turtle.color(player_colors[turtle])
    new_turtle.pu()
    new_turtle.setpos(x=-230, y=y)
    y += 30
    all_turtles.append(new_turtle)

if players:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >= 230:
            winner = turtle.pencolor()
            if single_or_multi == "s":
                if single_bet == winner:
                    mb.showinfo(message=f"You win! The winner was {winner}")
                    is_race_on = False
                else:
                    mb.showinfo(message=f"You lose. The winner was {winner}.")
                    is_race_on = False
            else:
                for player in player_bets:
                    if player_bets[player] == winner:
                        is_race_on = False
                        mb.showinfo(message=f"{player} won!")
                    else:
                        continue
        random_distance = random.randint(0, 10)
        turtle.fd(random_distance)

screen.exitonclick()
