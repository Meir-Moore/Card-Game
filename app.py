import time
import pydealer
from texttable import Texttable
from Players import Player
from tabulate import tabulate


# Get the player's name
def get_player_name():
    name = input("""Welcome to War card game!
    Please enter your name: """)

    while not name.isalpha():
        name = input("Please enter letters: ")

    return name


# Create player and computer instances
def create_players(name):
    player = Player()
    computer = Player()
    player.name = name
    computer.name = "Jarvis"
    return player, computer


# Function to create and shuffle the card deck
def card_deck(player, computer):
    deck = pydealer.Deck()
    hand = pydealer.Stack()

    hand.add(deck.deal(52))
    hand.shuffle()

    pack = list(hand)

    # Deal cards to both players
    for _ in range(26):
        player.add_card(pack.pop())
        computer.add_card(pack.pop())


# Function to display the current game table with player and computer decks
def table_game(player, computer):
    table_data = [["Name", "Deck"], [player.name, player.deck], [computer.name, computer.deck]]
    table = Texttable()
    table.add_rows(table_data)
    print(table.draw())


# Function to show the current cards being played
def show_cards(player, computer):
    text = f"{player.name} card: {player.card}"
    text2 = f"{computer.name} card : {computer.card}"
    table = [[text, text2]]
    output = tabulate(table, tablefmt='fancy_grid')
    print(output)


# Function to announce a war
def war_announce():
    text = "War!"
    table = [[text]]
    output = tabulate(table, tablefmt='fancy_grid')
    print(output)


# Function to play a round of War
def play_round(player, computer):
    player.hit_card()
    time.sleep(0.5)
    computer.hit_card()
    time.sleep(0.5)
    show_cards(player, computer)

    # Determine the winner of the round
    if player.card > computer.card:
        player.add_card(computer.card)
        player.add_card(player.card)
        time.sleep(0.5)
        player.win_round()

        # Check if computer's deck is empty
        if computer.deck < 1:
            table_game(player, computer)
            time.sleep(0.5)
            player.win_game()
            exit(0)
    elif player.card < computer.card:
        computer.add_card(player.card)
        computer.add_card(computer.card)
        time.sleep(0.5)
        computer.win_round()

        # Check if player's deck is empty
        if player.deck < 1:
            table_game(player, computer)
            time.sleep(0.5)
            computer.win_game()
            exit(0)
    elif player.card == computer.card:
        player.add_war_card(player.card)
        computer.add_war_card(computer.card)

        # Continue to play a war until a winner is determined
        while True:
            war_announce()
            time.sleep(0.5)
            war(player, computer)
            time.sleep(0.5)

            # Determine the winner of the war
            if player.card > computer.card:
                for c in computer.war_deck:
                    player.add_war_card(c)
                for c in player.war_deck:
                    player.add_card(c)
                time.sleep(0.5)
                player.win_war()
                computer.lose_war()
                break
            elif player
                        card < computer.card:
                for c in player.war_deck:
                    computer.add_war_card(c)
                for c in computer.war_deck:
                    computer.add_card(c)
                time.sleep(0.5)
                computer.win_war()
                player.lose_war()
                break


# Function to play a war
def war(player, computer):
    # If player's deck has 3 or fewer cards
    if player.deck <= 3:
        for _ in range(player.deck):
            time.sleep(0.5)
            player.hit_card()
            player.add_war_card(player.card)
            time.sleep(0.5)
            computer.hit_card()
            computer.add_war_card(computer.card)
        time.sleep(0.5)
        show_cards(player, computer)
    # If computer's deck has 3 or fewer cards
    elif computer.deck <= 3:
        for _ in range(computer.deck):
            time.sleep(0.5)
            computer.hit_card()
            computer.add_war_card(computer.card)
            time.sleep(0.5)
            player.hit_card()
            player.add_war_card(player.card)
        time.sleep(0.5)
        show_cards(player, computer)
    # If both players have more than 3 cards
    else:
        for _ in range(2):
            time.sleep(0.5)
            player.hit_card()
            player.add_war_card(player.card)
            time.sleep(0.5)
            computer.hit_card()
            computer.add_war_card(computer.card)
        time.sleep(0.5)
        player.hit_card()
        player.add_war_card(player.card)
        time.sleep(0.5)
        computer.hit_card()
        computer.add_war_card(computer.card)
        time.sleep(0.5)
        show_cards(player, computer)


def game():
    player_name = get_player_name()
    player, computer = create_players(player_name)
    card_deck(player, computer)
    table_game(player, computer)

    # Main game loop
    while True:
        try:
            hit_card = int(input("Type 1 to hit a card, type 2 for exit: "))
            if hit_card == 1:
                play_round(player, computer)
            elif hit_card == 2:
                print("Bye bye :)")
                break
            else:
                print("Error, type again!")
            time.sleep(0.6)
            table_game(player, computer)
            time.sleep(0.6)

            # Check if either player's deck is empty and end the game
            if computer.deck < 1:
                player.win_game()
                exit(0)
            elif player.deck < 1:
                computer.win_game()
                exit(0)
        except ValueError:
            print("Invalid key")


if __name__ == "__main__":
    game()
