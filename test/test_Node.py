import unittest

from mock import Mock


class MyTestCase(unittest.TestCase):

    def test_empty(self):
        self.assertIs(True, True)


if __name__ == '__main__':
    unittest.main()
