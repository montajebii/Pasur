import pytest
from project import deal_cards, capture_possible, calculate_score, find_sum_to_11


# Fixture to mock the deck of cards
@pytest.fixture
def mock_deck():
    return [(1, '♠'), (2, '♦'), (3, '♣'), (4, '♥'), (5, '♠'), (6, '♦'), (7, '♣'), (8, '♥')]


def test_deal_cards(mock_deck):
    # Testing if 4 cards are dealt and removed from the deck
    hand = deal_cards(mock_deck, 4)
    assert len(hand) == 4
    assert len(mock_deck) == 4  # 4 cards should be removed from the deck


def test_capture_possible_king():
    table_cards = [(13, '♠'), (1, '♦'), (7, '♣')]
    player_card = (13, '♣')  # King of Clubs
    captured_cards = capture_possible(player_card, table_cards)
    assert captured_cards == [(13, '♠')]  # Should capture only Kings


def test_capture_possible_queen():
    table_cards = [(12, '♦'), (1, '♥'), (7, '♠')]
    player_card = (12, '♠')  # Queen of Spades
    captured_cards = capture_possible(player_card, table_cards)
    assert captured_cards == [(12, '♦')]  # Should capture only Queens


def test_capture_possible_jack():
    table_cards = [(10, '♦'), (1, '♣'), (7, '♠'), (13, '♥')]
    player_card = (11, '♠')  # Jack of Spades
    captured_cards = capture_possible(player_card, table_cards)
    # Should capture everything except King
    assert captured_cards == [(10, '♦'), (1, '♣'), (7, '♠')]


def test_find_sum_to_11():
    table_cards = [(10, '♦'), (1, '♣'), (7, '♠'), (4, '♥')]
    player_card_value = 4
    result = find_sum_to_11(player_card_value, table_cards)
    assert result == [(7, '♠')]  # 4 + 7 = 11


def test_calculate_score():
    player_captured = [(2, '♣'), (10, '♦'), (1, '♠'), (11, '♦')]
    computer_captured = [(1, '♣'), (12, '♦')]
    player_surs = 1
    computer_surs = 0
    player_score, computer_score = calculate_score(
        player_captured, computer_captured, player_surs, computer_surs)

    assert player_score == 12  # 2♣ + 10♦ + 1 Ace + 1 Jack + 5 (Sur)
    assert computer_score == 1  # 1 Ace
