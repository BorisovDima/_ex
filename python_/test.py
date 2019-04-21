import unittest
import logging
import sys

logger = logging.getLogger('test')
logger.setLevel(logging.WARNING)
h = logging.StreamHandler(stream=sys.stdout)
h.setLevel(logging.WARNING)
logger.addHandler(h)

class Testim(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.logger = logging.getLogger('test')
        cls.logger.warning('start class')

    def setUp(self):
        self.logger.warning('start method')


    @unittest.skip
    def test_skip(self):
        self.assertTrue(0)

    def test_subtest(self):
        for i in range(6):
            with self.subTest(i=i):
                self.assertTrue(i % 2 == 0)
        with self.subTest('Zero'):
            self.assertTrue(0)

    def tearDown(self):
        self.logger.warning('End method')

    @classmethod
    def tearDownClass(cls):
        cls.logger.warning('End class')

# unittest.main(exit=False) # code exit 0
# unittest.main() # code exit 1
