import unittest
from substring_search import boyer_moore_search, knuth_morris_pratt_search, rabin_karp_search

class TestSubstringSearch(unittest.TestCase):
    def setUp(self):
        self.text = "Це тестовий рядок для пошуку підрядка у тексті."
        self.existing_substring = "пошуку"
        self.non_existing_substring = "відсутній"

    def test_boyer_moore_existing(self):
        self.assertEqual(boyer_moore_search(self.text, self.existing_substring), self.text.find(self.existing_substring))

    def test_boyer_moore_non_existing(self):
        self.assertEqual(boyer_moore_search(self.text, self.non_existing_substring), -1)

    def test_knuth_morris_pratt_existing(self):
        self.assertEqual(knuth_morris_pratt_search(self.text, self.existing_substring), self.text.find(self.existing_substring))

    def test_knuth_morris_pratt_non_existing(self):
        self.assertEqual(knuth_morris_pratt_search(self.text, self.non_existing_substring), -1)

    def test_rabin_karp_existing(self):
        self.assertEqual(rabin_karp_search(self.text, self.existing_substring), self.text.find(self.existing_substring))

    def test_rabin_karp_non_existing(self):
        self.assertEqual(rabin_karp_search(self.text, self.non_existing_substring), -1)

if __name__ == "__main__":
    unittest.main()