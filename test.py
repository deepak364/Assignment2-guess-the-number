import random

# writing and running the tests
import unittest
from game import GuessGame

class TestGuessGame(unittest.TestCase):

    # Functiom to test the random number generator
    def randomnumbergeneratortest(self):
        game = GuessGame()
        number = game.random()
        self.assertIsInstance(number, int)
        self.assertTrue(1000 <= number <= 9999)

    # Function to test the check function
    def checkguesstest(self):
        game = GuessGame()
        game.num = 5678
        result = game.check(5768)
        #if we run the above code it will give the following answer
        #2 circles and 2 x because:
        # 2 circles because 5 and 8 are correct and in the correct position
        # 2 x becaue 6 and 7 are correct but in the wrong position.
        self.assertEqual(result, "2 (circles) 2 (x)")

if __name__ == '__main__':
    # run all the test method
    unittest.main()
    