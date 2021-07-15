import random
from Players import Player
import pydealer
import os
from art import *
from tabulate import tabulate
from texttable import Texttable

player = Player()
computer = Player()

player.name = "Test"


def card_divider():
    for card in range(20):
        if card % 2 == 1:
            player.add_card(random.randint(1, 14))
        else:
            computer.add_card(random.randint(1, 14))


def war():
    print("War!")
    for card in range(2):
        player.hit_war_card()
        player.add_war_card(player.card)
    for card in range(2):
        computer.hit_war_card()
        computer.add_war_card(computer.card)
    player.hit_card()
    player.add_war_card(player.card)
    computer.hit_card()
    computer.add_war_card(player.card)


def show_cards():
    text = f"{player.name} card: {player.card}"
    text2 = f"{computer.name} card : {computer.card}"
    table = [[text, text2]]
    output = tabulate(table, tablefmt='pretty')
    print(output)


def table_game():
    table_data = [["Name", "Pile"], [player.name, player.deck], [computer.name, computer.deck]]
    table = Texttable()
    table.add_rows(table_data)
    print(table.draw())


deck = pydealer.Deck()
hand = pydealer.Stack()
print()
hand.add(deck.deal(52))
print(hand[1])

hand.shuffle()
print(hand[1])
pack = []


