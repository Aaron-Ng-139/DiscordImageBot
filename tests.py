import unittest
from responses import random_integer


class TestRandomInteger(unittest.TestCase):
    err_twoArgs = "Error: rand only takes 2 numerical arguments (rand #min #max)"
    err_ints = "Error: rand needs 2 integers (rand #min #max)"
    err_minMax = "Error: max cannot be less than min (rand #min #max)"
    
    def test_tooManyStrArguments(self):
        result = random_integer("rand a b c")
        self.assertEqual(result, self.err_twoArgs)
    
    def test_tooFewStrArguments(self):
        result = random_integer("rand a")
        self.assertEqual(result, self.err_twoArgs)
        
    def test_tooManyIntArguments(self):
        result = random_integer("rand 1 2 3 4")
        self.assertEqual(result, self.err_twoArgs)
    
    def test_tooFewIntArguments(self):
        result = random_integer("rand 321")
        self.assertEqual(result, self.err_twoArgs)
    
    def test_noIntegers(self):
        result = random_integer("rand a a")
        self.assertEqual(result, self.err_ints)
        
    def test_oneIntLeft(self):
        result = random_integer("rand 1 a")
        self.assertEqual(result, self.err_ints)
        
    def test_oneIntRight(self):
        result = random_integer("rand a 1")
        self.assertEqual(result, self.err_ints)
        
    def test_minOverMax(self):
        result = random_integer("rand 6 4")
        self.assertEqual(result, self.err_minMax)
        
    def test_minOverMax2(self):
        result = random_integer("rand 8322 202")
        self.assertEqual(result, self.err_minMax)
    
    def test_randIntFunctional(self):
        result = random_integer("rand 1 5")
        self.assertTrue(isinstance(result, int) and result >= 1 and result <= 5)
    
    def test_randIntBigNumbers(self):
        result = random_integer("rand 25 6000")
        self.assertTrue(isinstance(result, int) and result >= 25 and result <= 6000)
        
    def test_randIntRangeOfOne(self):
        result = random_integer("rand 1 1")
        self.assertEqual(result, 1)
        
    def test_randIntNegatives(self):
        result = random_integer("rand -5 -3")
        self.assertTrue(isinstance(result, int) and result >= -5 and result <= -3)
        
    def test_randIntNegatives2(self):
        result = random_integer("rand -5 2")
        self.assertTrue(isinstance(result, int) and result >= -5 and result <= 2)
        
    def test_randIntNegatives3(self):
        result = random_integer("rand -555 121")
        self.assertTrue(isinstance(result, int) and result >= -555 and result <= 121)
        
if __name__ == '__main__':
    unittest.main()