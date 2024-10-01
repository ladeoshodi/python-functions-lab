import unittest
import exercises


class TestFunctionLab(unittest.TestCase):
    def test_calculate_area_triangle(self):
        self.assertEqual(exercises.calculate_area_triangle(10, 5), 25.0)
        self.assertEqual(exercises.calculate_area_triangle(7, 3), 10.5)

    def test_simple_interest(self):
        self.assertEqual(exercises.simple_interest(1000, 5, 2), 100)
        self.assertEqual(exercises.simple_interest(1500, 3.5, 5), 262.5)

    def test_apply_discount(self):
        self.assertEqual(exercises.apply_discount(100, 25), 75)
        self.assertEqual(exercises.apply_discount(80, 10), 72)

    def test_convert_temperature(self):
        self.assertEqual(exercises.convert_temperature(0, "C"), 32.0)
        self.assertEqual(exercises.convert_temperature(32, "F"), 0.0)


if __name__ == '__main__':
    unittest.main()
