from mtgsdk import Card
from mtgsdk import Set
from mtgsdk import Type
from mtgsdk import Supertype
from mtgsdk import Subtype
from mtgsdk import Changelog
from new_deck_methods import *


class Deck:
    def __init__(self, title, format, commander = None, cards = []):
        self.title = title
        self.format = format
        self.count = 0
        self.cards = cards
        self.commander = commander
        if format == "commander":
            self.add_cards(commander) #sets commander as first card, and ensure you dont end up in a 101 card scenario
            self.deck_color = commander['colorIdentity']
    
    def current_list(self):
        print(f"{self.cards}")
        

    def add_cards(self, new_card):
        if format == "standard":
            if self.count < 60:
                self.cards.append(new_card)
                print(f"{self.count}")
                self.count=+ 1
            else:
                raise ("Deck already full!")
        elif format == "commander":
            if self.count < 100:
                self.cards.append(new_card)
                print(f"{self.count}")
                self.count=+ 1
            else:
                raise ("Deck already full!")
            
    def remove_cards(self, card):
        try:
            self.cards.remove(card)
            self.count = self.count - 1
            return
        except ValueError:
            print("No such card exists!")
            return

    def landfill(self):
        if self.format == "commander":
            to_fill = 100 - self.count
        else:
            print("Landfill only supported in commander decks")
            return
        ratio = to_fill // len(self.deck_color)
        if self.deck_color == []:
            for i in range(to_fill):
                self.add_cards_complex(fuzzy="wastes")
            return "deck filled with {to_fill} wastes"
        for i in range(len(self.deck_color) - 1):
            if self.deck_color[i] == "W":
                while i < ratio:
                    self.add_cards_complex("plains")
                    i+= 1
            if self.deck_color[i] == "B":
                while i < ratio:
                    self.add_cards_complex("swamp")
                    i+= 1
            if self.deck_color[i] == "R":
                while i < ratio:
                    self.add_cards_complex("mountain")
                    i+= 1
            if self.deck_color[i] == "G":
                while i < ratio:
                    self.add_cards_complex("forest")
                    i+= 1
            if self.deck_color[i] == "U":
                while i < ratio:
                    self.add_cards_complex("island")
                    i+= 1
        if to_fill % len(self.deck_color) != 0:
            remainder = to_fill % len(self.deck_color) - 1
            if self.deck_color[0] == "W":
                while i < remainder:
                    self.add_cards_complex("plains")
                    i+= 1
            if self.deck_color[0] == "B":
                while i < remainder:
                    self.add_cards_complex("swamp")
                    i+= 1
            if self.deck_color[0] == "R":
                while i < remainder:
                    self.add_cards_complex("mountain")
                    i+= 1
            if self.deck_color[0] == "G":
                while i < remainder:
                    self.add_cards_complex("forest")
                    i+= 1
            if self.deck_color[0] == "U":
                while i < remainder:
                    self.add_cards_complex("island")
                    i+= 1
        print(f"deck filled with {to_fill} lands")
        return 
        

    def export(self):
        placeholder = 0

    #todo  landfill convert_deck_to_list