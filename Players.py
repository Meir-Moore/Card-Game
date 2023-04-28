from tabulate import tabulate  # Import tabulate library for output formatting


class Player:
    # Define a Player class

    def __init__(self):
        # Initialize instance variables
        name = ""             # player name
        card = 0              # current card
        cards = []            # list of cards in player's deck
        war_deck = []         # list of cards in player's war deck
        deck = 0              # number of cards in player's deck
        self.name = name      # initialize instance variables
        self.card = card
        self.cards = cards
        self.war_deck = war_deck
        self.deck = deck

    def win_round(self):
        # Output a message to indicate that the player has won the round
        text = f"{self.name} wins!"
        table = [[text]]
        output = tabulate(table, tablefmt="fancy_grid")
        print(output)

    def win_war(self):
        # Output a message to indicate that the player has won a war
        text = f"{self.name} wins the war!"
        table = [[text]]
        output = tabulate(table, tablefmt="fancy_grid")
        print(output)
        # Clear the war deck since the player has won
        self.war_deck = []

    def lose_war(self):
        # Clear the war deck since the player has lost
        self.war_deck = []

    def win_game(self):
        # Output a congratulatory message to indicate that the player has won the game
        text = f"{self.name} win the game!\nSee you next time! :)"
        table = [[text]]
        output = tabulate(table, tablefmt='pretty')
        print(output)

    def balance(self):
        # Output a table with the player's name and the number of cards remaining in their deck
        output = [[self.name, self.deck]]
        return output

    def add_card(self, card):
        # Add a card to the player's deck
        self.cards.insert(0, card)
        self.deck = len(self.cards)

    def add_war_card(self, card):
        # Add a card to the player's war deck
        self.war_deck.insert(0, card)

    def hit_card(self):
        # Remove the last card from the player's deck and output the card that has been drawn
        self.card = self.cards.pop()
        self.deck = len(self.cards)
        print(f"{self.name}")
        output = tabulate([[f"{self.card}"]], tablefmt="fancy_grid")
        print(output)

    def hit_war_card(self):
        # Remove the last card from the player's deck and output a placeholder card with an "X" value to indicate a war
        self.card = self.cards.pop()
        self.deck = len(self.cards)
        table = [["X"]]
        output = tabulate(table, tablefmt="fancy_grid")
        print(output)

