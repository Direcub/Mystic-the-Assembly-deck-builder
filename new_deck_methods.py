from deck_object import Deck
import scrython

def create_new_deck():
    print("What would you like to name it?")
    deck_title = input()
    format = get_format()
    if format == "commander":
        print("what will the commander be?")
        commander_query = input()
        commander = scrython.cards.Named(fuzzy="{commander_query}")
        return Deck(deck_title, format, commander)
    else:
        return Deck(deck_title, format)
    

def get_format():
    print("What format would you like, commander or standard")
    answer = input()
    if answer != "commander" or answer != "standard":
        print("format not recongized")
        get_format()
    return answer

def open_existing_deck(deck_name):
    placeholder = 0

    #todo open_existing_deck