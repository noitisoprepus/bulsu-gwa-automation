import unittest
import gwa_calculator

class TestGWACalc(unittest.TestCase):
    
    def test_calculate_gwa(self):
        weighted_grades = [1.0, 1.5, 2.25]
        total_units = 9
        self.assertEqual(gwa_calculator.calculate_gwa(weighted_grades, total_units), 0.5278)

        weighted_grades = [2.5, 4.0, 5.0]
        total_units = 9
        self.assertEqual(gwa_calculator.calculate_gwa(weighted_grades, total_units), 1.2778)

        weighted_grades = []
        total_units = 0
        self.assertEqual(gwa_calculator.calculate_gwa(weighted_grades, total_units), 0)

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

    def test_login_and_scrape(self):
        pass

if __name__ == "__main__":
    unittest.main()