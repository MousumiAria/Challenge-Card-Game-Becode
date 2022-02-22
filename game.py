class Board:
    def __init__(self, players:int,turn_count:int,active_cards:int,history_cards:int):
        """Constructor our class"""
        self.players = players
        self.turn_count = turn_count
        self.active_cards = active_cards
        self.history_cards = history_cards