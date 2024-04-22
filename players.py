import random

from card import Card


class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.score = 0

    def add_card(self, deck, flag):
        new_card = Card(random.randrange(0, 4), random.randrange(1, 14), flag)
        while not new_card.is_card_in_deck(deck):
            new_card = Card(random.randrange(0, 4), random.randrange(1, 14), flag)
        self.cards.append(new_card)
        self.count_score()
        print(str(self.name) + str(new_card.ret_value()))


        return new_card.suit, new_card.value

    def throw_cards(self):
        self.cards = []
        self.score = 0

    def count_score(self):
        score_temp = [i.value for i in self.cards]
        score_temp.sort(reverse=True)
        result = 0

        for i in score_temp:
            if i >= 10:
                result += 10
            elif 2 <= i < 10:
                result += i
            else:
                if result + 10 > 21:
                    result += 1
                else:
                    result += 10
        self.score = result

    def cards_info(self):
        return [i.ret_value() if i.visibility else "?" for i in self.cards]





