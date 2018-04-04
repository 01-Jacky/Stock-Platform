import unittest

from app.data_access import iextrading_wrapper

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        # self.widget = Widget('The widget')
        pass

    def tearDown(self):
        # self.widget.dispose()
        pass

    def test_got_closing_data(self):
        json_data = iextrading_wrapper.get_1_month('aapl','1m')
        self.assertGreater(len(json_data), 1)
        self.assertTrue(isinstance(json_data[0]['close'], float))

if __name__ == '__main__':
    unittest.main()