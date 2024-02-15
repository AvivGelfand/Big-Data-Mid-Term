# Filename: test_count_top_diff_freq_words.py
import unittest
import os
from count_top_diff_freq_words import find_top_diff_freq_words

class TestCountTopDiffFreqWords(unittest.TestCase):
    def setUp(self):
        # Create temporary files for testing
        self.file1 = 'temp_file1.txt'
        self.file2 = 'temp_file2.txt'
        with open(self.file1, 'w') as f:
            f.write('apple banana apple\norange banana')
        with open(self.file2, 'w') as f:
            f.write('banana orange banana\napple apple')

    def tearDown(self):
        # Delete temporary files after testing
        os.remove(self.file1)
        os.remove(self.file2)

    def test_find_top_diff_freq_words(self):
        expected = [('orange', 0.25), ('banana', 0.25)]  # Example expected outcome
        result = find_top_diff_freq_words(self.file1, self.file2, 2)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
