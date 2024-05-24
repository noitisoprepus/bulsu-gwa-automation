import gwa_calculator
import unittest
from unittest.mock import patch

class TestGWACalc(unittest.TestCase):
    
    def test_calculate_gwa(self):
        weighted_grades = [1.0, 1.5, 2.25]
        total_units = 3
        self.assertEqual(gwa_calculator.calculate_gwa(weighted_grades, total_units), 1.5833)

        weighted_grades = [2.5, 4.0, 5.0]
        total_units = 3
        self.assertEqual(gwa_calculator.calculate_gwa(weighted_grades, total_units), 3.8333)

        weighted_grades = []
        total_units = 0
        self.assertEqual(gwa_calculator.calculate_gwa(weighted_grades, total_units), None)

    def test_check_latin_honors(self):
        computed_gwa = 1.75
        grades = [1.0, 1.5, 2.25]
        self.assertEqual(gwa_calculator.check_latin_honors(computed_gwa, grades), "Cum Laude")

        computed_gwa = 1.45
        grades = [1.0, 1.5, 2.25]
        self.assertEqual(gwa_calculator.check_latin_honors(computed_gwa, grades), "Magna Cum Laude")

        computed_gwa = 1
        grades = [1.0, 1.5, 2.0]
        self.assertEqual(gwa_calculator.check_latin_honors(computed_gwa, grades), "Summa Cum Laude")

        computed_gwa = 1
        grades = [1.0, 1.5, 2.75]
        self.assertEqual(gwa_calculator.check_latin_honors(computed_gwa, grades), None)

        computed_gwa = 1.76
        grades = [1.0, 1.0, 1.0]
        self.assertEqual(gwa_calculator.check_latin_honors(computed_gwa, grades), None)

    @patch('gwa_calculator.login_and_scrape')
    def test_main(self, mock_login_and_scrape):
        mock_login_and_scrape.return_value = ([1.0, 1.5, 2.25], [1.0, 1.5, 2.25], 3)
        grades, weighted_grades, total_units = gwa_calculator.login_and_scrape("username", "pass")
        computed_gwa = gwa_calculator.calculate_gwa(weighted_grades, total_units)
        honors = gwa_calculator.check_latin_honors(computed_gwa, grades)
        self.assertEqual(computed_gwa, 1.5833)
        self.assertEqual(honors, "Cum Laude")

if __name__ == "__main__":
    unittest.main()