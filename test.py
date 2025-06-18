import unittest
import main


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(main.func(main.sleep(1)), 5)  # add assertion here


if __name__ == '__main__':
    unittest.main()
