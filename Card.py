class Card:
    m_rankChars = "23456789TJQKA"
    m_suitChars = "hdcs"

    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank

    def CharToRank(self, c):
        if c == 'A':
            return 12
        elif c == 'K':
            return 11
        elif c == 'Q':
            return 10
        elif c == 'J':
            return 9
        elif c == 'T':
            return 8
        elif c == '9':
            return 7
        elif c == '8':
            return 6
        elif c == '7':
            return 5
        elif c == '6':
            return 4
        elif c == '5':
            return 3
        elif c == '4':
            return 2
        elif c == '3':
            return 1
        elif c == '2':
            return 0
        return -1

    def CharToSuit(self, s):
        if s == 's':
            return 3
        elif s == 'c':
            return 2
        elif s == 'd':
            return 1
        elif s == 'h':
            return 0
        return -1

    def RankToChar(self, rank):
        return Card.m_rankChars[rank]

    def SuitToChar(self, suit):
        return Card.m_suitChars[suit]

