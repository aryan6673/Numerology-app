import unittest
from numerology import NumerologyProApp  # Import your app class
import datetime

class TestNumerology(unittest.TestCase):

    def setUp(self):
        """Set up an instance of the Numerology app before each test."""
        self.app = NumerologyProApp()

    def test_life_path_number(self):
        """Test life path number calculation."""
        birth_date = datetime.datetime(2001, 12, 15)  # Example date: 15th Dec 2001
        self.assertEqual(self.app.calculate_life_path(birth_date), 3)

    def test_destiny_number(self):
        """Test destiny number calculation."""
        self.assertEqual(self.app.calculate_destiny("Aryan Kumar"), 3)

    def test_soul_number(self):
        """Test soul urge number calculation."""
        self.assertEqual(self.app.calculate_soul("Aryan Kumar"), 9)

    def test_personality_number(self):
        """Test personality number calculation."""
        self.assertEqual(self.app.calculate_personality("Aryan Kumar"), 3)

    def test_birthday_number(self):
        """Test birthday number calculation."""
        birth_date = datetime.datetime(2001, 12, 15)  # 15th December 2001
        self.assertEqual(self.app.calculate_birthday(birth_date), 6)

if __name__ == "__main__":
    unittest.main()
