import unittest
from hash_table import HashTable

class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.hash_table = HashTable(10)
        self.hash_table.insert("apple", 10)
        self.hash_table.insert("orange", 20)
        self.hash_table.insert("banana", 30)

    def test_insert_and_get(self):
        self.assertEqual(self.hash_table.get("apple"), 10)
        self.assertEqual(self.hash_table.get("orange"), 20)
        self.assertEqual(self.hash_table.get("banana"), 30)

    def test_update_value(self):
        self.hash_table.insert("apple", 15)
        self.assertEqual(self.hash_table.get("apple"), 15)

    def test_delete_existing_key(self):
        self.assertTrue(self.hash_table.delete("apple"))
        self.assertIsNone(self.hash_table.get("apple"))

    def test_delete_non_existing_key(self):
        self.assertFalse(self.hash_table.delete("grape"))

    def test_get_non_existing_key(self):
        self.assertIsNone(self.hash_table.get("grape"))

if __name__ == "__main__":
    unittest.main()