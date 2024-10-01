import unittest
import exercises

class TestFunctionLab(unittest.TestCase):
    def test_calculate_area_triangle(self):
        self.assertEqual(exercises.calculate_area_triangle(10, 5), 25.0)
        self.assertEqual(exercises.calculate_area_triangle(7,3), 10.5)
        
        

if __name__ == '__main__':
    unittest.main()