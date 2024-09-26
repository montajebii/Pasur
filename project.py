import os
from pyfiglet import figlet_format
from termcolor import cprint
import random
from itertools import combinations


# Define the deck of cards (1-13 represents Ace to King, and use symbols for suits)
suits = ["♣", "♦", "♥", "♠"]  # Clubs, Diamonds, Hearts, Spades
ranks = list(range(1, 14))  # 1 to 13 (Ace to King)
deck = [(rank, suit) for rank in ranks for suit in suits]


# Main game loop
def main():

    # Shuffle and deal
    random.shuffle(deck)
    player_hand = deal_cards(deck, 4)
    computer_hand = deal_cards(deck, 4)
    table_cards = deal_cards(deck, 4)

    # Initialize capture piles and Pasur tracker
    player_captured = []
    computer_captured = []

    player_surs = 0
    computer_surs = 0

    os.system("cls" if os.name == "nt" else "clear")
    cprint(figlet_format("Pasur", font="slant"), "green")
    print("\n--- Pasur Game Starts ---")

    while player_hand or computer_hand:
        if player_hand:
            print("\nPlayer's turn")
            player_turn(player_hand, table_cards, player_captured, player_surs)

        if computer_hand:
            print("\nComputer's turn")
            computer_turn(computer_hand, table_cards, computer_captured, computer_surs)

        # Deal new cards if both hands are empty
        if not player_hand and deck:
            player_hand = deal_cards(deck, 4)

        if not computer_hand and deck:
            computer_hand = deal_cards(deck, 4)

    print("\n--- Game Over ---")

    # Calculate and display final scores
    player_score, computer_score = calculate_score(
        player_captured, computer_captured, player_surs, computer_surs)

    print(f"Player's Score: {player_score}")
    print(f"Computer's Score: {computer_score}")

    if player_score > computer_score:
        print("You win!")
    elif computer_score > player_score:
        print("Computer wins!")
    else:
        print("It's a tie!")


# Function to deal cards
def deal_cards(deck, num):
    hand = random.sample(deck, num)
    for card in hand:
        deck.remove(card)
    return hand


# Function to handle a player's turn
def player_turn(player_hand, table_cards, player_captured, player_surs):
    print(f"\nTable cards: {print_hand(table_cards)}")
    print(f"Your cards: {print_hand(player_hand)}\n")

    # Player selects a card
    while True:
        try:
            card_index = int(input("Select a card to play (1-4): ")) - 1
            if 0 <= card_index < len(player_hand):
                selected_card = player_hand[card_index]
                break
            else:
                print("Invalid choice, please select a valid card.")
        except ValueError:
            print("Invalid input, please enter a number.")

    # Check for capture
    captured_cards = capture_possible(selected_card, table_cards)

    if captured_cards:
        print(f"Captured: {print_hand(captured_cards)}")
        for card in captured_cards:
            table_cards.remove(card)
            player_captured.append(card)
        if len(table_cards) == 0:
            print("You made a Sur!")
            player_surs += 1
        captured_cards.append(
            selected_card
        )  # Player's card is also added to captured cards
    else:
        print("No capture possible.")
        table_cards.append(selected_card)

    player_hand.remove(selected_card)


# Function for the computer to make its move
def computer_turn(computer_hand, table_cards, computer_captured, computer_surs):
    print("\nComputer's turn...")

    for card in computer_hand:
        captured_cards = capture_possible(card, table_cards)
        if captured_cards:
            print(
                f"Computer played {format_card(card[0], card[1])} and captured {print_hand(captured_cards)}"
            )
            for captured in captured_cards:
                table_cards.remove(captured)
                computer_captured.append(captured)
            if len(table_cards) == 0:
                print("Computer made a Sur!")
                computer_surs += 1
            computer_hand.remove(card)
            computer_captured.append(card)
            return

    # No capture, play a random card
    selected_card = random.choice(computer_hand)
    print(
        f"Computer played {format_card(selected_card[0], selected_card[1])}, but no capture was made."
    )
    computer_hand.remove(selected_card)
    table_cards.append(selected_card)


# Function to print the cards in a hand
def print_hand(hand):
    return ", ".join([format_card(rank, suit) for rank, suit in hand])


# Function to convert rank numbers to card faces (e.g., 1 -> 'A', 11 -> 'J', etc.)
def format_card(rank, suit):
    if rank == 1:
        rank_str = "A"
    elif rank == 11:
        rank_str = "J"
    elif rank == 12:
        rank_str = "Q"
    elif rank == 13:
        rank_str = "K"
    else:
        rank_str = str(rank)
    return f"{rank_str}{suit}"


# Function to calculate if a capture is possible
def capture_possible(player_card, table_cards):
    """
    Check if a capture is possible according to the rules:
    - By pairing a King or Queen from hand with a King or Queen on the table.
    - By addition: capturing cards from the table that sum to 11.
    - By playing a Jack: capturing all cards on the table except Kings and Queens.

    Args:
        player_card: Tuple (rank, suit) representing the card played by the player.
        table_cards: List of tuples representing the cards on the table.

    Returns:
        A list of cards that can be captured. Empty list if no capture is possible.
    """
    rank, suit = player_card
    captured_cards = []

    # If the player plays a Jack (J), it captures all cards except Kings and Queens
    if rank == 11:  # Jacks
        captured_cards = [
            card for card in table_cards if card[0] not in {12, 13}
        ]  # Exclude Queens (12) and Kings (13)
        return captured_cards

    # If the player plays a King (K), it captures any King on the table
    if rank == 13:  # Kings
        captured_cards = [
            card for card in table_cards if card[0] == 13
        ]  # Only capture Kings
        return captured_cards

    # If the player plays a Queen (Q), it captures any Queen on the table
    if rank == 12:  # Queens
        captured_cards = [
            card for card in table_cards if card[0] == 12
        ]  # Only capture Queens
        return captured_cards

    # For pip cards (A=1, 2=2, ..., 10=10), we need to find combinations that sum to 11
    if rank < 11:  # Only pip cards can sum to 11 (Ace to 10)
        captured_cards = find_sum_to_11(rank, table_cards)

    return captured_cards


def find_sum_to_11(player_value, table_cards):
    """
    Find a combination of cards on the table that sum to 11 with the player's card.

    Args:
        player_value: The numeric value of the card played by the player.
        table_cards: List of tuples representing the cards on the table.

    Returns:
        A list of cards that sum to 11 with the player's card, or an empty list if no such combination exists.
    """

    # Convert table cards to just their numeric values
    table_values = [card[0] for card in table_cards]

    # Try to find combinations of 1, 2, or more cards that sum to 11 with the player's card
    for r in range(1, len(table_values) + 1):
        for combo in combinations(table_values, r):
            if sum(combo) + player_value == 11:
                # Find the actual cards (rank, suit) that correspond to this combination of values
                return [card for card in table_cards if card[0] in combo]

    return []  # No valid combination found


# Scoring system based on Pasur rules
def calculate_score(player_captured, computer_captured, player_surs, computer_surs):
    """
    Calculate and print the scores based on the cards captured and surs made during the game.

    Args:
        player_captured: List of cards captured by the player.
        computer_captured: List of cards captured by the computer.
        player_surs: Number of Surs made by the player.
        computer_surs: Number of Surs made by the computer.
    """
    player_score = 0
    computer_score = 0

    # Points for capturing 2♣ (2 points)
    player_score += 2 if (2, "♣") in player_captured else 0
    computer_score += 2 if (2, "♣") in computer_captured else 0

    # Points for capturing 10♦ (3 points)
    player_score += 3 if (10, "♦") in player_captured else 0
    computer_score += 3 if (10, "♦") in computer_captured else 0

    # Points for capturing 7 or more ♣ cards (7 points)
    player_clubs = sum(1 for rank, suit in player_captured if suit == "♣")
    computer_clubs = sum(1 for rank, suit in computer_captured if suit == "♣")

    if player_clubs >= 7:
        player_score += 7
    if computer_clubs >= 7:
        computer_score += 7

    # Points for capturing Aces (each Ace is 1 point)
    player_score += sum(1 for rank, suit in player_captured if rank == 1)
    computer_score += sum(1 for rank, suit in computer_captured if rank == 1)

    # Points for capturing Jacks (each Jack is 1 point)
    player_score += sum(1 for rank, suit in player_captured if rank == 11)
    computer_score += sum(1 for rank, suit in computer_captured if rank == 11)

    # Points for Pasur (Surs) - 5 points for each Sur
    player_score += player_surs * 5
    computer_score += computer_surs * 5

    return player_score, computer_score


if __name__ == "__main__":
    main()
