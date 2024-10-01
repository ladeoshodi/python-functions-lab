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

    def test_sum_to(self):
        self.assertEqual(exercises.sum_to(6), 21)
        self.assertEqual(exercises.sum_to(10), 55)

    def test_largest(self):
        self.assertEqual(exercises.largest(1, 2, 3), 3)
        self.assertEqual(exercises.largest(10, 4, 2), 10)

    def test_calculate_tip(self):
        self.assertEqual(exercises.calculate_tip(50, 20), 10)

    def test_product(self):
        self.assertEqual(exercises.product(2, 5, 5), 50)
        self.assertEqual(exercises.product(-1, 4), -4)

    def test_basic_calculator(self):
        self.assertEqual(exercises.basic_calculator(10, 5, 'subtract'), 5)
        self.assertEqual(exercises.basic_calculator(10, 5, 'add'), 15)
        self.assertEqual(exercises.basic_calculator(10, 5, 'multiply'), 50)
        self.assertEqual(exercises.basic_calculator(10, 5, 'divide'), 2)


if __name__ == '__main__':
    unittest.main()
