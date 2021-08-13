import os, sys
sys.path.append(os.path.dirname(__file__) + '/../')

from new import NEW
import unittest

@NEW.parse
def new_func(a = NEW.new([]), b='append me'):
    a.append(b)
    return a

class TestNewParser(unittest.TestCase):

    def test_empty_func(self):
        self.assertEqual(new_func(), ['append me'])
    
    def test_kw_func(self):
        self.assertEqual(new_func(b='and me'), ['and me'])
        self.assertEqual(new_func(a=['append me'], b='and me'), ['append me', 'and me'])
    
    def test_args_func(self):
        self.assertEqual(new_func(['append']), ['append', 'append me'])
        self.assertEqual(new_func(['append'], 'appendix'), ['append', 'appendix'])

if __name__ == '__main__':
    unittest.main()