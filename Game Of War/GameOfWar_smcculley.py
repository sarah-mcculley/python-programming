import cards, games

class War_Card(cards.Card):
    """ A War Card """

    def __init__(self):
        super().__init__()
        self.__available = True

    @property
    def value(self):
        if self.is_face_up:
            v = War_Card.RANKS.index(self.rank) + 1
            if self.rank == "A":
                v = 14
        return v

    @property
    def available(self):
        return self.__available

    def discard(self):
        self.__available = False


class War_Deck(cards.Deck):
    """ A War Deck """
    def populate(self):
        for suit in War_Card.SUITS:
            for rank in War_Card.RANKS:
                self.cards.append(War_Card(rank, suit))

class War_Hand(cards.Hand):
    """A War Hand """
    def __init__(self, name):
        super(War_Hand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":\t" + super(War_Hand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep


class War_Player(War_Hand):
    """ A War Player """

    def win_round(self):
        print(self.name, "wins round.")

    def lose_round(self):
        print(self.name, "loses round.")

    def win_game(self):
        print(self.name, "wins game.")

    def lose_game(self):
        print(self.name, "loses game.")

    def is_empty(self):
        return len(self.cards) == 0

    def flip(self):
        return self.cards[0]


class War_Round(cards.Hand):
    """ The Cards at War"""


class War_Game(object):

    def __init__(self, names):
        self.players = []
        for name in names:
            player = War_Player(name)
            self.players.append(player)

        self.deck = War_Deck
        self.deck.populate()
        self.deck.shuffle()

    def flip(self):
        for player in self.players:
            player.flip()


    def play(self):
        #deal half the deck to each player
        self.deck.deal(self.players, per_hand = 26)

        players_empty = []
        for player in self.players:
            players_empty.append(player.is_empty())

        while not all(players_empty):
            self.flip()




def main():
    print("\t\tWelcome to War!\n")

    names = []
    number = games.ask_number("How many players? (2): ", low = 2, high = 3)
    for i in range(number):
        name = input("Enter player name: ")
        names.append(name)

    game = War_Game(names)

    again = None
    while again != "n":
        game.play()
        again = games.ask_yes_no("\nDo you want to play again?: ")

main()
input("\n\nPress the enter key to exit.")




