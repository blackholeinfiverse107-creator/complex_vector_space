import unittest
import sys

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    loader = unittest.TestLoader()
    suite = loader.discover('tests')
    result = runner.run(suite)
    if result.wasSuccessful():
        print("\nSUCCESS\n")
    else:
        print("\nFAILURE\n")

