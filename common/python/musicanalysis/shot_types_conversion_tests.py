import unittest
from musicanalysis.shot_types_conversion import *
import os


class ShotTypesConver(unittest.TestCase):
    def test_manual_analysis_csv_path(self):
        result = extract_sequence_from_manual_analysis(f'{os.path.dirname(__file__)}\\templates\\ariana_grande\\manual_analysis.csv')
        print(result)