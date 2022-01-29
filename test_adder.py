import unittest
import interpreter


class TestAdder(unittest.TestCase):
    # noinspection PyPep8Naming
    def __init__(self, methodName='runTest'):
        super().__init__(methodName=methodName)
        self.lines = interpreter.load_file(interpreter.SOURCE_FILE)

    def add(self, x: int, y: int) -> int:
        args = {
            'X': x,
            'Y': y,
        }
        stepthrough = interpreter.execute_lines(self.lines, args)
        output = stepthrough[-1][2]['X']
        return output

    def test_example(self):
        self.assertEqual(self.add(14, 35), 49)

    def test_rigorous(self):
        for x in range(255 + 1):
            for y in range(255 - x):
                self.assertEqual(self.add(x, y), x + y)


if __name__ == '__main__':
    unittest.main()
