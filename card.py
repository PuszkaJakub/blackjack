class Card:
    def __init__(self, suit, value, visibility):
        self.suit = suit
        self.value = value
        self.visibility = visibility

    def ret_value(self):
        return card_suit_parser.get(self.suit), card_value_parser.get(self.value)

    def is_card_in_deck(self, deck):
        return any(self.value == cards_left for cards_left in deck[self.suit])


card_value_parser = {
    1: 'ace',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'jack',
    12: 'queen',
    13: 'king'
}
card_suit_parser = {
    0: 'hearts',
    1: 'diamonds',
    2: 'spades',
    3: 'clubs'
}


def new_deck():
    return [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]]
