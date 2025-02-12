import scrython

class Deck:
    def __init__(self, title, format, commander = None):
        self.title = title
        self.format = format
        self.count = 0
        self.cards = []
        self.commander = commander

    #todo set_commander, add_card, remove_card, convert_deck_to_list