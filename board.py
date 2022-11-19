import math
from deck import HouseDeck, CheckDeck
from player import Player

class Board:

    def __init__(self, num_players, starting_coins):
        self.player_dict = {i: Player(i, starting_coins) for i in range(num_players)}
        self.properties = HouseDeck()
        self.checks = CheckDeck()
        self.num_players = num_players
    
    def displayCards(self, cards, card_type='house'):
        """prints cards to terminal"""
        if card_type == 'house':
            suit = '🏠'
        else:
            suit = '💰'

        lines = [[] for i in range(9)]
        for index, card in enumerate(cards):
            if card >= 10:
                space = ''
            else:
                space = ' '

            lines[0].append('┌─────────┐')
            lines[1].append('│{}{}       │'.format(card, space))  # use two {} one for char, one for space or char
            lines[2].append('│         │')
            lines[3].append('│         │')
            lines[4].append('│    {}   │'.format(suit))
            lines[5].append('│         │')
            lines[6].append('│         │')
            lines[7].append('│       {}{}│'.format(space, card))
            lines[8].append('└─────────┘')

        result = []
        for index, line in enumerate(lines):
            result.append(''.join(lines[index]))
        print('\n'.join(result))

    def bidRound(self):
        """
        Property cards are selected and players place bids on those properties.
        """
        property_cards = self.properties.deal(self.num_players)
        players_out_round = [0] * self.num_players
        curr_player = 0
        bids = [0] * self.num_players
        # loop until only 1 player left
        while sum(players_out_round) != self.num_players - 1:
            self.displayCards(property_cards)
            bid = self.player_dict[curr_player].placeBid(bids[curr_player], max(bids))
            if bid == 0:
                # if player passes, they get the lowest remaining property.
                # They get back half of their current bid rounded down
                self.player_dict[curr_player].addProperty(property_cards.pop(-1))
                self.player_dict[curr_player].addCoins(math.floor(-1 * bids[curr_player] / 2))
                players_out_round[curr_player] = 1
            else:
                # player bids some amount
                bids[curr_player] = bid
            
            # next player is the player next in players_in_round where entry is 0
            while True:
                curr_player = (curr_player + 1) % self.num_players
                if not players_out_round[curr_player]: 
                    break 
            
            print(curr_player)
            print(players_out_round)
             
        # last player gets the last property and no coins back
        self.player_dict[curr_player].addProperty(property_cards.pop(-1))
        self.player_dict[curr_player].addCoins(-1 * bids[curr_player])
    
    def displayBoardState(self):
        for i, player in self.player_dict.items():
            print("Player {} has {} coins and following properties:".format(i, player.coins))
            self.displayCards(player.properties)
            print()

if __name__ == "__main__":
    NUM_PLAYERS = 4
    STARTING_COINS = 15
    B = Board(4, 15)
    B.bidRound()
    B.displayBoardState()

