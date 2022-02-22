class Symbol:
   # icon = ['\u2666', '\u2665', '\u2663', '\u2660']
   # value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self, color: str, icon):
        """Constructor our class"""
        self.color = color
        self.icon = icon

    def __str__(self):
        return f"{Symbol.color[self.color]}{Symbol.icon[self.icon]}"


class Card(Symbol):
    def __init__(self, color, icon, value: str):
        super().__init__(color, icon)
        """Constructor our class"""
        self.value = value

    def __str__(self):
        return f"{Card.value[self.value]}{Symbol.icon[self.icon]}"
