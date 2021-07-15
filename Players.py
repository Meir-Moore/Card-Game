from tabulate import tabulate


class Player:

    def __init__(self):
        name = ""
        card = 0
        cards = []
        war_deck = []
        deck = 0
        self.name = name
        self.card = card
        self.cards = cards
        self.war_deck = war_deck
        self.deck = deck

    def win_round(self):
        text = f"{self.name} wins!"
        table = [[text]]
        output = tabulate(table, tablefmt="fancy_grid")
        print(output)

    def win_war(self):
        text = f"{self.name} wins the war!"
        table = [[text]]
        output = tabulate(table, tablefmt="fancy_grid")
        print(output)
        self.war_deck = []

    def lose_war(self):
        self.war_deck = []

    def win_game(self):
        text = f"{self.name} win the game!\nSee you next time! :)"
        table = [[text]]
        output = tabulate(table, tablefmt='pretty')
        print(output)

    def balance(self):
        output = [[self.name, self.deck]]
        return output

    def add_card(self, card):
        self.cards.insert(0, card)
        self.deck = len(self.cards)

    def add_war_card(self, card):
        self.war_deck.insert(0, card)

    def hit_card(self):
        self.card = self.cards.pop()
        self.deck = len(self.cards)
        print(f"{self.name}")
        output = tabulate([[f"{self.card}"]], tablefmt="fancy_grid")
        print(output)

    def hit_war_card(self):
        self.card = self.cards.pop()
        self.deck = len(self.cards)
        table = [["X"]]
        output = tabulate(table, tablefmt="fancy_grid")
        print(output)
