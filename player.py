from card import Card
import random

class Player:
    def __init__(self, cards: [], turn_count: int = 0, number_of_cards: int = 0, pname=str):
        """Constructor our class"""

        self.pname = pname
        self.cards = cards
        self.turn_count = turn_count
        self.number_of_cards = number_of_cards[0]
        self.history = [cards]

    def play(self):
        card = random.choice(self.cards)
        self.history.append(card)
        print(self.pname + self.turn_count + " played: " + card.value + card.icon)

class Deck:
    #def __init__(self, cards[], icon:str, value:str):
        """Constructor our class"""
        #self.cards = cards
    #   self.icon = icon
    #  self.value = value
    #  icon = ['\u2666', '\u2665', '\u2663', '\u2660']
    #  value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    #  self.deck=[]

        #cards:[]


        def __init__(self):
          self.icons = ['\u2666', '\u2665', '\u2663', '\u2660']
          self.values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
          self.cards = []

        def fill_deck(self):
            for icon in self.icons:
                for value in self.values:
                    self.cards.append(Card(icon, value))

        def shuffle(self):
            random.shuffle(self.cards)

        def distribute(self, players: []):
            num = (self.cards / len(players))
            index = 0
            for card in self.cards:
                players[index].Cards.Append(card)
                index = index + 1
                if index >= len(players) - 1:
                    index = 0





