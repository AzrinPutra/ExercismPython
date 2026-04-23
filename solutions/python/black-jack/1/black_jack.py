"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    face_cards = {'J': 10, 'Q': 10, 'K': 10, 'A': 1}
    card_upper = card.upper()
    if card_upper in face_cards:
        return face_cards[card_upper]
    if card.isdigit() and 2 <= int(card) <= 10:
        return int(card)
    else:
        raise ValueError(f"Invalid card")


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    value_1 = value_of_card(card_one)
    value_2 = value_of_card(card_two)

    if value_1 == value_2:
        return (card_one, card_two)
    if value_1 > value_2:
        return card_one
    else:
        return card_two

def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for an upcoming ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    face_cards = {'J': 10, 'Q': 10, 'K': 10}
    current_hand = [card_one, card_two]
    current_hand_value = []
    
    for card in current_hand:
        if card.upper() == 'A':
            card = 11
            current_hand_value.append(card)
        else:
            if card in face_cards:
                current_hand_value.append(face_cards[card])
            else:
                current_hand_value.append(int(card))

    if 10 < sum(current_hand_value) <= 21:
        return 1
    else:
        return 11
    

def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    face_cards = {'J': 10, 'Q': 10, 'K': 10}
    current_hand = [card_one, card_two]
    current_hand_value = []

    for card in current_hand:
        if card.upper() == 'A':
            card = 11
            current_hand_value.append(card)
        else:
            if card in face_cards:
                current_hand_value.append(face_cards[card])
            else:
                current_hand_value.append(int(card))

    if sum(current_hand_value) == 21:
        return True
    else:
        return False

def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    face_cards = {'J': 10, 'Q': 10, 'K': 10, 'A': 11}

    if higher_card(card_one, card_two) == card_one or higher_card(card_one, card_two) == card_two:
        return False
    else:
        return True

def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    face_cards = {'J': 10, 'Q': 10, 'K': 10, 'A': 1}
    current_hand = [card_one, card_two]
    current_hand_value = []
    
    for card in current_hand:
        if card in face_cards:
            current_hand_value.append(face_cards[card])
        else:
            current_hand_value.append(int(card))

    if 9 <= sum(current_hand_value) <= 11:
        return True
    else:
        return False
