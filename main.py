from scrython import *
from new_deck_methods import *
from deck_object import Deck

def main():
    print("Would you like to make a 'new deck' or 'edit' an existing one?")
    mode = input()
    if mode == "new deck":
        working_deck = create_new_deck() 
    elif mode == "edit":
        print("which deck would you like to edit?(Exact names only.)")
        working_deck = open_existing_deck(input())
    #todo adding cards, removing cards, filling with land, and calling the non-existant export function

main()