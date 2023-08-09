import unittest
from tracemem import TraceMem

class TestTraceMem(unittest.TestCase):

    def test_init(self):
        mem = TraceMem((1048576, 2097152))
        self.assertEqual(mem.current, 1)
        self.assertEqual(mem.peak, 2)

    def test_str(self):
        mem = TraceMem((1048576, 2097152))
        self.assertEqual(str(mem), "current=1.00, peak=2.00")

if __name__ == "__main__":
    unittest.main()