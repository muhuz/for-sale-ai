
class Player:

    def __init__(self, name, starting_coins):
        self.name = name
        self.coins = starting_coins
        self.properties = []

    def placeBid(self, player_bid, max_bid):
        """
        player_bid (int): The bid the player has made in total
        max_bid (int): The last highest bid which represents what the
        current player must match 
        """
        print("Player ({}), Your turn to bid. Your current bid is {}. The highest bid is {}".format(self.name, player_bid, max_bid))
        # if max_bid is higher than player can afford then they must pass
        if max_bid >= self.coins:
            print("You don't have enough to pass the current bid so you must pass!")
            return 0
        # get user input
        else:
            while True:
                try:
                    bid = int(input('Place a Bid: '))
                    if bid != 0 and not (bid >= (max_bid + 1) and (bid <= self.coins)):
                        raise ValueError
                    break
                except:
                    print('Valid Options are 0 or a value between {} and {}:'.format(max_bid + 1, self.coins))
        return bid
    
    def bid(self, n):
        """Player places a bid of n coins"""
        if n > self.coins:
            raise Exception("Player does not have enough coins")
        else:
            self.coins -= n
    
    def selectProperty(self, p):
        """Player selects a property then own"""
        if p not in self.properties:
            raise Exception("Player does not have this property")
        else:
            p_idx = self.properties.index(p)
            return self.properties.pop(p_idx)

    def addCoins(self, c):
        """"Give the player c coins"""
        self.coins += c
    
    def addProperty(self, p):
        """Give the player property p"""
        insert_idx = 0
        while insert_idx < len(self.properties):
            if self.properties[insert_idx] < p:
                break
            insert_idx += 1
        self.properties.insert(insert_idx, p)

    def __str__(self):
        return "Player {} has {} coins and {} properties".format(self.name, self.coins, self.properties)
