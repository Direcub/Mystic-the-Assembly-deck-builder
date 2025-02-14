from mtgsdk import Card
from mtgsdk import Set
from mtgsdk import Type
from mtgsdk import Supertype
from mtgsdk import Subtype
from mtgsdk import Changelog


def main():
    card = Card.where(name= 'Black Lotus')
    wtf = card.array()
    wtf = wtf[0]
    print(f"{wtf['legalities']}")
    return


main()