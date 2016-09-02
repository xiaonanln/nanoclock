import unittest
from nanoclock import nanoclock
import time

from nanoclock import SECOND, MILLISECOND, MICROSECOND
print SECOND

class Test(unittest.TestCase):
    def test_nanoclock(self):
        t0 = nanoclock()
        t1 = nanoclock()
        time.sleep(1)
        t2 = nanoclock()
        print t0, t1, t2, t1-t0, t2 - t1

        self.assertTrue(t0 <= t1 <= t0+MILLISECOND)
        self.assertTrue(t1 + SECOND <= t2 <= t1 + SECOND + 100 * MILLISECOND)

if __name__ == '__main__':
    unittest.main()

