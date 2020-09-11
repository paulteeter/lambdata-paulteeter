import unittest
import pandas as pd
from pt_lambdata.ds_utilities import Nose


class TestBoogerUtilities(unittest.TestCase):
    """
    Unit Test for date extraction
    """

    def test_date_extract(self):
        df = pd.DataFrame({
            'Date' : ['12-25-1990', '7-4-2008', '3-13-2013']
            })
        boogs = Nose(df)
        new_df = boogs.booger_picker('Date')
        self.assertEqual(new_df['Year'][0], 1990)
        self.assertEqual(new_df['Month'][0], 12)
        self.assertEqual(new_df['Day'][1], 4)

if __name__ == '__main__':
    unittest.main()