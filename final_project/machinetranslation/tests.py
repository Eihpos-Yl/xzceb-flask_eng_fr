import unittest
from translator import englishToFrench, frenchToEnglish

class TestTranslationFunctions(unittest.TestCase):

    def test_english_to_french_null_input(self):
        # Test for null input
        self.assertIsNone(englishToFrench(None))

    def test_french_to_english_null_input(self):
        # Test for null input
        self.assertIsNone(frenchToEnglish(None))

    def test_english_to_french_hello(self):
        # Test for translation of 'Hello'
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertNotEqual(englishToFrench('Hello'), 'Au revoir')

    def test_french_to_english_bonjour(self):
        # Test for translation of 'Bonjour'
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertNotEqual(frenchToEnglish('Bonjour'), 'Goodbye')

if __name__ == '__main__':
    unittest.main()
