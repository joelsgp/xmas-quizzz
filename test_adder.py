import unittest
import interpreter


class TestAdder(unittest.TestCase):
    @staticmethod
    def add(x: int, y: int) -> int:
        args = {
            'X': x,
            'Y': y,
        }
        stepthrough = interpreter.run_file(interpreter.SOURCE_FILE, args)
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
