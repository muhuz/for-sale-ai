import random

class Deck:

    def reset(self):
        """resets the deck"""
        self.deck = [0] * 30

    def draw(self, n):
        """randomly choose n cards from the deck"""
        open_idxs = [i for i, v in enumerate(self.deck) if v == 0]
        chosen_idxs = random.sample(open_idxs, k=n)
        for j in chosen_idxs:
            self.deck[j] = 1
        return sorted(self._idx_to_value(chosen_idxs), reverse=True)

    def deal(self, n):
        """draw n cards and return them"""
        idxs = self.draw(n)
        return self._idx_to_value(idxs)
    
    def _idx_to_value(self, idxs):
        pass


class HouseDeck(Deck):
    """Deck of property cards ranging from 1 to 30"""
    
    def __init__(self):
        self.deck = [0] * 30
    
    def _idx_to_value(self, idxs):
        """Converts a list of idxs to the proper card values"""
        return [i + 1 for i in idxs]

class CheckDeck(Deck):
    """Deck of 30 check cards. 2 copies of each card, 0 and 2 through 15"""

    def __init__(self):
        self.deck = [0] * 30
    
    def _idx_to_value(self, idxs):
        """Converts a list of idxs to the proper card values"""
        converted_vals = []
        for i in idxs:
            if i // 2 > 0:
                converted_vals.append(i // 2 + 1)
            else:
                converted_vals.append(0)
        return converted_vals
