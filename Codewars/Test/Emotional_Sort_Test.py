from Emotional_Sort_6_kyu import sort_emotions
import unittest

class EmotionalSort(unittest.TestCase):
    def test_1(self):
        arr = [':D', ':|', ':)', ':(', ':D']
        result = [':D', ':D', ':)', ':|', ':(']
        self.assertEqual(sort_emotions(arr, True), result)
    
    def test_2(self):
        arr = [':D', ':|', ':)', ':(', ':D']
        result = [':D', ':D', ':)', ':|', ':(']
        self.assertEqual(sort_emotions(arr, False), result[::-1])
    
    def test_3(self):
        arr = []
        result = []
        self.assertEqual(sort_emotions(arr, True), result)

if __name__ == "__main__":
    unittest.main()