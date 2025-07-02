import unittest
from generated.code.bmi_calculator import calculate_bmi

class TestBMI(unittest.TestCase):
    def test_bmi(self):
        self.assertAlmostEqual(calculate_bmi(70, 175), 22.86, places=2)

if __name__ == "__main__":
    unittest.main()
