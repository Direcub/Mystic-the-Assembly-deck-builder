import scrython

class Deck:
    def __init__(self, title, format, commander = None):
        self.title = title
        self.format = format
        if format == "standard":
            self.count = 0
        else:
            self.count = 1
        self.cards = []
        self.commander = commander

    def add_cards(self, card):
        if format == "standard":
            if self.count < 60:
                self.cards.append(scrython.cards.Named(fuzzy=card))
            else:
                print("Deck already full!")
                return
        elif format == "commander":
            if self.count < 100:
                self.cards.append(scrython.cards.Named(fuzzy=card))
            else:
                print("Deck already full!")
                return 
    def remove_cards(self, card):
        try:
            self.cards.remove(scrython.cards.Named(fuzzy=card))
        except ValueError:
            print("No such card exists!")
            return

    def landfill(self):

    def export(self):

    #todo  landfill convert_deck_to_list