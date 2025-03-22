from deck_object import Deck
from mtgsdk import Card
from mtgsdk import Set
from mtgsdk import Type
from mtgsdk import Supertype
from mtgsdk import Subtype
from mtgsdk import Changelog

def create_new_deck():
    deck_title = input("What would you like to name it?\n")
    format = get_format()
    if format == "commander":
        commander = set_commander()
        return Deck(deck_title, format, commander)
    else:
        return Deck(deck_title, format)
    

def get_format():       ##standalone function to enable recursion in case format isnt correct
    answer = input("What format would you like, commander or standard\n")
    if answer == "commander" or answer == "standard":
        return answer
    print("format not recongized")
    return get_format()

def open_existing_deck(deck_name):
    placeholder = 0

    #todo open_existing_deck

def set_commander(): #standalone function to enable recursion in case the card isnt found
    commander_query = input("What will the commander be? Spelling is important\n")
    try:
        query = Card.where(name=commander_query)
        demon_chants = query.array()            #strips card
        commander = demon_chants[0]
        return commander
    except:
        print("commander not found")
        return set_commander()

def add_cards_complex(deck):
    rst = "Would you like to [add] or [remove] cards, [landfill], [export], or [exit]?\n"
    mode = input("type the name of the card you would like to add, when you are done, simply enter [done]\n")
    while mode != "done":
        try:
            search = Card.where(name= mode) 
            scoped_search = search.array() #strips down search query object into just the card
            card = scoped_search[0]
            legal = card['legalities']
            if card['colorIdentity'] not in deck.deck_color:
                print("color identity mismatch")       #color checking
                return input(f"{rst}")
            if legal[0]['format'] != 'commander':
                if legal[1]['legality'] == 'Banned':
                    print("Card is banned in current format") # legality checking
                    return input(f"{rst}")
            if legal[0]['legality'] == 'Banned':
                print("Card is banned in current format")
                return input(f"{rst}")
            deck.add_cards(card) #simple add statement
            print("added")
        except:
            return input(f"{rst}")
        mode = input() # here to ask for next card 
    return input(f"{rst}")

def remove_cards_complex(deck):
    rst = "Would you like to [add] or [remove] cards, [landfill], [export], or [exit]?\n"
    card = input("what card would you like to remove?\n")
    try:
        deck.remove_cards(card)
        deck.count-= 1
    except:
        print("card not found")
        return input(f"{rst}")