import time
import pydealer
from texttable import Texttable
from Players import Player
from tabulate import tabulate

name = input("""Welcome to War card game!
Please enter your name: """)

while not name.isalpha():
    name = input("Please enter letters: ")

player = Player()
computer = Player()
player.name = name
computer.name = "Jarvis"


def game():
    card_deck()
    table_game()
    while True:
        try:
            hit_card = int(input("Type 1 to hit a card, type 2 for exit: "))
            if hit_card == 1:
                play_round()
            elif hit_card == 2:
                print("Bye bye :)")
                break
            else:
                print("Error, type again!")
            time.sleep(0.6)
            table_game()
            time.sleep(0.6)
            if computer.deck < 1:
                player.win_game()
                exit(0)
            elif player.deck < 1:
                computer.win_game()
                exit(0)
        except ValueError:
            print("Invalid key")


def card_deck():
    deck = pydealer.Deck()
    hand = pydealer.Stack()

    hand.add(deck.deal(52))

    hand.shuffle()
    pack = []
    for c in range(52):
        pack.append(hand[c])

    for c in range(26):
        player.add_card(pack.pop())
        computer.add_card(pack.pop())


def play_round():
    player.hit_card()
    time.sleep(0.5)
    computer.hit_card()
    time.sleep(0.5)
    show_cards()
    if player.card > computer.card:
        player.add_card(computer.card)
        player.add_card(player.card)
        time.sleep(0.5)
        player.win_round()
        if computer.deck < 1:
            table_game()
            time.sleep(0.5)
            player.win_game()
            exit(0)
    elif player.card < computer.card:
        computer.add_card(player.card)
        computer.add_card(computer.card)
        time.sleep(0.5)
        computer.win_round()
        if player.deck < 1:
            table_game()
            time.sleep(0.5)
            computer.win_game()
            exit(0)
    elif player.card == computer.card:
        player.add_war_card(player.card)
        computer.add_war_card(computer.card)
        while True:
            war_announce()
            time.sleep(0.5)
            war()
            time.sleep(0.5)
            if player.card > computer.card:
                for c in computer.war_deck:
                    player.add_war_card(c)
                for c in player.war_deck:
                    player.add_card(c)
                time.sleep(0.5)
                player.win_war()
                computer.lose_war()
                break
            elif player.card < computer.card:
                for c in player.war_deck:
                    computer.add_war_card(c)
                for c in computer.war_deck:
                    computer.add_card(c)
                time.sleep(0.5)
                computer.win_war()
                player.lose_war()
                break


def war():
    if player.deck <= 3:
        for count in range(player.deck):
            time.sleep(0.5)
            player.hit_card()
            player.add_war_card(player.card)
            time.sleep(0.5)
            computer.hit_card()
            computer.add_war_card(computer.card)
        time.sleep(0.5)
        show_cards()
    elif computer.deck <= 3:
        for count in range(computer.deck):
            time.sleep(0.5)
            computer.hit_card()
            computer.add_war_card(computer.card)
            time.sleep(0.5)
            player.hit_card()
            player.add_war_card(player.card)
        time.sleep(0.5)
        show_cards()
    else:
        for count in range(2):
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
        show_cards()


def show_cards():
    text = f"{player.name} card: {player.card}"
    text2 = f"{computer.name} card : {computer.card}"
    table = [[text, text2]]
    output = tabulate(table, tablefmt='fancy_grid')
    print(output)


def table_game():
    table_data = [["Name", "Deck"], [player.name, player.deck], [computer.name, computer.deck]]
    table = Texttable()
    table.add_rows(table_data)
    print(table.draw())


def war_announce():
    text = "War!"
    table = [[text]]
    output = tabulate(table, tablefmt='fancy_grid')
    print(output)


game()
