from deck_object import Deck
from mtgsdk import Card
from mtgsdk import Set
from mtgsdk import Type
from mtgsdk import Supertype
from mtgsdk import Subtype
from mtgsdk import Changelog

def create_new_deck():
    deck_title = "new_deck" #input("What would you like to name it?\n")
    format = "commander" #get_format()
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
    return get_format()

def open_existing_deck(deck_name):
    placeholder = 0

    #todo open_existing_deck

def set_commander():
    commander_query = input("What will the commander be? Spelling is important\n")
    try:
        query = Card.where(name=commander_query)
        demon_chants = query.array()
        commander = demon_chants[0]
        return commander
    except:
        print("commander not found")
        return set_commander()

def add_cards_complex(deck):
    mode = input("type of the name of the card you would like to add, when you are done, simply enter [done]\n")
    while mode != "done":
        try:
            search = Card.where(name= mode)
            scoped_search = search.array()
            card = scoped_search[0]
            legal = card['legalities']
            if card['colorIdentity'] not in deck.deck_color:
                print("color identity mismatch")
                return input("Would you like to [add] or [remove] cards, [landfill], [export], or [exit]?\n")
            if legal[0]['format'] != 'commander':
                if legal[1]['legality'] == 'Banned':
                    print("Card is banned in current format")
                    return input("Would you like to [add] or [remove] cards, [landfill], [export], or [exit]?\n")
            if legal[0]['legality'] == 'Banned':
                print("Card is banned in current format")
                return input("Would you like to [add] or [remove] cards, [landfill], [export], or [exit]?\n")
            deck.add_cards(card)
            print("added")
        except:
            return input("Would you like to [add] or [remove] cards, [landfill], [export], or [exit]?\n")
        mode = input()
    return input("Would you like to [add] or [remove] cards, [landfill], [export], or [exit]?\n")