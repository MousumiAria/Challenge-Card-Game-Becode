from card import Symbol
from card import Card
from player import Player
from player import Deck
import random

class Board:
    def __init__(self, players: list, turn_count: int, active_cards: int, history_cards: list):
        """Constructor our class"""
        self.players = players
        self.turn_count = turn_count
        self.active_cards = active_cards
        self.history_cards = history_cards

        # Create 4 input
        name1 = input("Name of player-1:")
        name2 = input("Name of player-2:")
        name3 = input("Name of player-3:")
        name4 = input("Name of player-4:")

        # Create 4 Object of Players
        p1 = Player(name1)
        p2 = Player(name2)
        p3 = Player(name3)
        p4 = Player(name4)

        self.players.append(p1)
        self.players.append(p2)
        self.players.append(p3)
        self.players.append(p4)


    def start_game(self):




