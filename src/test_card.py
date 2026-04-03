import unittest
from card_obj import Card

class TestCard(unittest.TestCase):
    def test_basic(self):
        card_string = str(Card("Strike", 1))
        expected = "Card(name=Strike, energy_cost=1, hand_position=0, draw=None, enhancement=None)"
        self.assertEqual(expected, card_string)

    def test_full(self):
        card_string = str(Card("Generic", 3, 6, 1, "Sharp 2"))
        expected = "Card(name=Generic, energy_cost=3, hand_position=6, draw=1, enhancement=Sharp 2)"
        self.assertEqual(card_string, expected)