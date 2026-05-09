import unittest
import functionplayground

class TestCubeFunction(unittest.TestCase):
    def test_that_cube_function_exists(self):
        functionplayground.cube(3)
