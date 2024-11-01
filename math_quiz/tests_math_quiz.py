import unittest
from math_quiz import random_Integer, random_Operator, compute


class TestMathGame(unittest.TestCase):

    def test_random_Integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_Integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_Operator(self):
        for _ in range(50):
            self.assertTrue(random_Operator() in ['+', '-', '*'])

    def test_compute(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (8, 7, '*', '8 * 7', 56),
                (15, 3, '-', '15 - 3', 12),
                (-9, 2, '+', '-9 + 2', -7),
                (4, 8, '-', '4 - 8', -4),
                (-1, 14, '*', '-1 * 14', -14),
                (-4, -5, '*', '-4 * -5', 20)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = compute(num1, num2, operator)
                self.assertTrue(problem == expected_problem and answer == expected_answer)

if __name__ == "__main__":
    unittest.main()
