from deck_object import Deck
import scrython

def create_new_deck():
    deck_title = input("What would you like to name it?\n")
    format = get_format()
    if format == "commander":
        commander = set_commander()
        return Deck(deck_title, format, commander)
    else:
        return Deck(deck_title, format)
    

def get_format():
    answer = input("What format would you like, commander or standard\n")
    if answer == "commander" or answer == "standard":
        return answer
    print("format not recongized")
    get_format()

def open_existing_deck(deck_name):
    placeholder = 0

    #todo open_existing_deck

def set_commander():
    commander_query = input("What will the commander be? Spelling is important\n")
    try:
        commander = scrython.cards.Named(fuzzy=commander_query)
        return commander
    except:
        print("commander not found")
        set_commander()
