import unittest
from translator import translateEnglishToFrench,translateFrenchToEnglish

class TestingTranslation(unittest.TestCase):


    def test_translateEnglishToFrench(self):
        self.assertEqual(translateEnglishToFrench(''), 'Bonjour')
        self.assertEqual(translateEnglishToFrench('Hello'), 'Bonjour')

    def test_translateFrenchToEnglish(self):
        self.assertEqual(translateFrenchToEnglish(''), 'Hello')
        self.assertEqual(translateFrenchToEnglish('Bonjour'), 'Hello')


if __name__ == '__main__':
    unittest.main()