import unittest
import sys
from src.GameEngine import GameEngine 

class GameEngineTest(unittest.TestCase):
    def test_should_return_combination_of_4chars(self):
        gameEngine = GameEngine();
        combination = gameEngine.getCombination();
        self.assertEqual(4, len(combination));
    def test_should_return_combination_of_4chars_with_random_chars_from_a_to_f(self):
        gameEngine = GameEngine();
        combination = gameEngine.getCombination();
        letters = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0};
        for letter in combination:
            letters[letter] += 1;
        count = 0
        while gameEngine.getCombination() == combination:
            if count == 10:
                raise Exception("No difference in combination")
            count += 1;
    def test_should_give_hint(self):
        gameEngine = GameEngine();
        self.assertEqual('++++', gameEngine.hint('ABCD', 'ABCD'));
        self.assertEqual('+++ ', gameEngine.hint('ABCF', 'ABCD'));
        self.assertEqual('--- ', gameEngine.hint('BCDE', 'ABCD'));
    def test_end_reached(self):
        gameEngine = GameEngine();
        self.assertFalse(gameEngine.endReached(1));
        self.assertTrue(gameEngine.endReached(8));
    def test_equals(self):
        gameEngine = GameEngine();
        self.assertTrue(gameEngine.equals("ABCD", "ABCD"));
        self.assertFalse(gameEngine.equals("BCDE", "ABCD"));

if __name__ == '__main__':
    unittest.main()
