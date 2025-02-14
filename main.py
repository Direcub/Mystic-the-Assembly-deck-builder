from mtgsdk import Card
from mtgsdk import Set
from mtgsdk import Type
from mtgsdk import Supertype
from mtgsdk import Subtype
from mtgsdk import Changelog
from new_deck_methods import *
from deck_object import Deck

def main():
    mode = "new deck" #input("Would you like to make a [new deck] or [edit] an existing one?\n")
    if mode == "new deck":
        working_deck = create_new_deck() 
    elif mode == "edit":
        working_deck = open_existing_deck(input("which deck would you like to edit?(Exact names only.)\n"))
    action = input("Deck configured! Would you like to [add] or [remove] cards, [landfill], [export], or [exit]?\n")
    while action == "add":
        action = add_cards_complex(working_deck)
    while action == "remove":
        action = remove_cards_complex(working_deck)
    while action == "landfill":
        working_deck.landfill()
        action = input("Would you like to [add] or [remove] cards, [landfill], [export], or [exit]?\n")
    while action == "export":
        working_deck.export()
        action = input("Would you like to [add] or [remove] cards, [landfill], [export], or [exit]?\n")
    while action == "exit":
        return
    #todo removing cards, importing, and exporting

main()