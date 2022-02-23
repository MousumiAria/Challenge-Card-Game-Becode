class Symbol:
   # icon = ['\u2666', '\u2665', '\u2663', '\u2660']
   # value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self, color: str, icon:str):
        """Constructor our class"""
        self.color = color
        self.icon = icon
        icons = ['\u2666', '\u2665', '\u2663', '\u2660']
        colors = ['red', 'green']


    def __str__(self):
        return f"{Symbol.color[self.color]}{Symbol.icon[self.icon]}"


class Card(Symbol):
    def __init__(self, color: str, icon: chr, value: str):
        super().__init__(color, icon)
        """Constructor our class"""
        #self.values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.value = value

    def __str__(self):
        return f"{self.value}, {self.icon}, {self.color}"

card1 = Card("red" , "heart", "6")
card2 = Card(1, 1, 1)
print(card1, card2)




