import random
import time

NEWDECK = {"card 2": 4, "card 3": 4, "card 4": 4, "card 5": 4, "card 6": 4,
            "card 7": 4, "card 8": 4, "card 9": 4, "card 10": 4, "card J": 4, 
            "card Q": 4, "card K": 4, "card A": 4}

def opp_move(deck, player_hand, opp_hand, player_points, opp_points):
    # Temp value if turn is repeated
    if_card = False
    # Randomly select a card from from the hand
    selected_card = random.choice(list(opp_hand.keys()))
    print(f"Opponent: Do you have any {selected_card}s?")
    time.sleep(1)

    # Check if player has the card
    if selected_card in player_hand:
        print("You: Yes")
        time.sleep(1)
        opp_hand, player_hand = transfer_cards(opp_hand, player_hand, selected_card)
        if_card = True
    else:
        print("You: No")
        time.sleep(1)
        deck, opp_hand, card = draw_card(deck, opp_hand)
        if card is None:
            print("*No more cards for opponent to draw.*")
        else:
            print("*Opponent drew a card.*")
            #if card == selected_card:
            #if_card = True
        time.sleep(1)

    # If card has value of 4 then remove from hand and add 1 point
    opp_hand, opp_points, is_pair = check_for_pairs(opp_hand, opp_points, False)
     # If pair is made, display points
    if is_pair:
        display_points(player_points, opp_points)

    # Check score to see if game end
    if (player_points + opp_points) == 13:
        return deck, player_hand, opp_hand, player_points, opp_points

    # Check to see if hand is empty. If so, draw
    deck, player_hand, opp_hand = check_if_empty(deck, player_hand, opp_hand)

    # If guess card correctly, repeat turn
    if if_card:
        return opp_move(deck, player_hand, opp_hand, player_points, opp_points)

    # Return values
    return deck, player_hand, opp_hand, player_points, opp_points

def player_move(deck, player_hand, opp_hand, player_points, opp_points):
    # Temp value if turn is repeated
    if_card = False
    # Ask player to select a card to go fishing for
    selected_card = ask_card(player_hand)
    print(f"\nYou: Do you have any {selected_card}s?")
    time.sleep(1)

    # Check if opponent has the card
    if selected_card in opp_hand:
        print("Opponent: Yes")
        time.sleep(1)
        player_hand, opp_hand = transfer_cards(player_hand, opp_hand, selected_card)
        if_card = True
    else:
        print("Opponent: No")
        time.sleep(1)
        deck, player_hand, card = draw_card(deck, player_hand)
        if card is None:
            print("*No more cards in deck to draw.*")
        else:
            print(f"*You drew {card}.*")
        time.sleep(1)

    # If card has value of 4 then remove from hand and add 1 point
    player_hand, player_points, is_pair = check_for_pairs(player_hand, player_points, False)
     # If pair is made, display points
    if is_pair:
        display_points(player_points, opp_points)

    # Check score to see if game end
    if (player_points + opp_points) == 13:
        return deck, player_hand, opp_hand, player_points, opp_points

    # Check to see if hand is empty. If so, draw
    deck, player_hand, opp_hand = check_if_empty(deck, player_hand, opp_hand)

    # If guess card correctly, repeat turn
    if if_card:
        return player_move(deck, player_hand, opp_hand, player_points, opp_points)

    # Return values
    return deck, player_hand, opp_hand, player_points, opp_points

def load_cards():
    # Copy newdeck to current game deck
    deck = NEWDECK
    # Declare player and opponent (computer) hands
    player_hand = {}
    opp_hand = {}

    # Randomly load player and opponent hands (7 cards) taking turns drawing starting with player
    for _ in range (7):
        deck, player_hand, _ = draw_card(deck, player_hand)
        deck, opp_hand, _ = draw_card(deck, opp_hand)

    # Return deck, player hand, and opponent (computer) hand as dictionaries
    return deck, player_hand, opp_hand

def ask_card(player_hand):
    # Create a loop to continuously ask for an input until a correct card is selected
    while True:
        # Ask user what card to select and give example
        time.sleep(1)
        print("\n*Please select a card from you hand to go fishing for.*")
        print(f"Your hand contains: {player_hand}*")
        rand_card_in_hand = next(iter(player_hand))
        
        selected_card = input(f"*example... type: {rand_card_in_hand}*\n")

        # Check if card syntax correct
        if selected_card in player_hand:
            break
        # If not, ask again
        else:
            print("\n*You do not have this card. Please try again.*")

    # Return which card user selected
    return selected_card

def transfer_cards(main_hand, other_hand, selected_card):
    # Remove the cards from other hand and increase amount in main hand
    card_amount = main_hand[selected_card] + other_hand[selected_card]
    del other_hand[selected_card]
    main_hand[selected_card] = card_amount

    # Notify player of what and how many cards were transfered
    print(f"*{selected_card} has been transferred.*")
    time.sleep(1)

    # Return both hands after cards are transfered
    return main_hand, other_hand

def check_for_pairs(hand, points, is_pair):
    # Create dict to add values to since we do not want to remove items during iterations when removing pairs
    hand_copy = {}

    # Check if hand has pairs of 4
    for key, value in hand.items():
        # If so, remove the set and increase points by 1
        if value == 4:
            points += 1
            is_pair = True
            print(f"*A pair of {key} has been made.*")
            time.sleep(1)
        # Make a copy hand of cards not in pairs of 4 to return
        else:
            hand_copy[key] = value

    # Return passed hand and points
    return hand_copy, points, is_pair

def check_if_empty(deck, player_hand, opp_hand):
    # Draw a card if hand is empty
    if not player_hand:
        deck, hand, card = draw_card(deck, player_hand)
        if not card == None:
            print(f"*You drew {card}.*")
    if not opp_hand:
        deck, hand, card = draw_card(deck, opp_hand)
        if not card == None:
            print("*Opponent drew a card.*")
    time.sleep(1)
    
    # Return deck, and passed hand
    return deck, player_hand, opp_hand

def draw_card(deck, hand):
    # Check if the deck is empty
    if not deck:
        print("*The deck is empty. No more cards to draw.*")
        time.sleep(1)
        return deck, hand, None

    # Randomly select a card from deck
    card = random.choice(list(deck.keys()))
    # Remove 1 of the card from the deck
    deck[card] -= 1
    # If card in deck value is 0, remove the card from deck
    if deck[card] == 0:
        del deck[card]
    # If card in hand, add 1 to card count
    if card in hand.keys():
        hand[card] += 1 
    # Else add the card to the hand
    else:
        hand[card] = 1

    # Return the updated deck and hand
    return deck, hand, card

def display_points(player_points, opp_points):
    print("Player points: ", player_points)
    print("Opponent points: ", opp_points)
    time.sleep(1)

def declare_winner(player_points, opp_points):
    # Declare winner
    print("\n\n============================")
    if player_points > opp_points:
        print("YOU WON!")
    else:
        print("You lose. Try again.")
    print("============================")   

def main():

    # Declare deck, hands, and points
    deck, player_hand, opp_hand = load_cards()    
    player_points, opp_points = 0, 0

    # Check for pairs at start
    player_hand, player_points, is_pair = check_for_pairs(player_hand, player_points, False)
    opp_hand, opp_points, is_pair = check_for_pairs(opp_hand, opp_points, False)
    display_points(player_points, opp_points)

    # Loop turns until all 13 pairs have been made
    while True:
        deck, player_hand, opp_hand, player_points, opp_points = player_move(deck, player_hand, opp_hand, player_points, opp_points)
        if (player_points + opp_points) == 13:
            break
        deck, player_hand, opp_hand, player_points, opp_points = opp_move(deck, player_hand, opp_hand, player_points, opp_points)
        if (player_points + opp_points) == 13:
            break

    declare_winner(player_points, opp_points)



# === Main Driver ===
print("\n\nWelcome to Go Fish!\n")
main()