import unittest
from src.example_package import example

class ExampleTest(unittest.TestCase):

    def test(self):
        self.assertEqual(2,example.add_one(1))