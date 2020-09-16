class Card:

    def __init__(self, suit=None, rank=None):
        suits = ['Diamond', 'Club', 'Heart', 'Spade']
        ranks = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

        if suit in suits and rank in ranks:
            self.rank = rank
            self.suit = suit

        else:
            raise Exception("Card does not exist")

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit