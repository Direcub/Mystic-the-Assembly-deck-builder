from scrython import *
from new_deck_methods import *
from deck_object import Deck

def main():
    mode = input("Would you like to make a 'new deck' or 'edit' an existing one?\n")
    if mode == "new deck":
        working_deck = create_new_deck() 
    elif mode == "edit":
        working_deck = open_existing_deck(input("which deck would you like to edit?(Exact names only.)\n"))
    action = input("Deck configured! Would you like to [add] or [remove] cards, [landfill], or [export] this list?")
    while action == "add":
        action = add_cards_complex(working_deck)
    while action == "remove":
        action = remove_cards_complex(working_deck)
    while action == "landfill":
        lands_filled = working_deck.landfill()
        action = input()
    while action == "export":
        working_deck.export()
    #todo  removing cards, filling with land, and calling the non-existant export function

main()