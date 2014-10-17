#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

# Here's our "unit".
def InitDB():
    return 0

# Here's our "unit tests".
class InitDBTests(unittest.TestCase):

    def testcreate(self):
        self.failUnless(whatever(val))

    def testinsert(self):
        self.failIf(whatever(val))

    def testdelete(self):
        self.failIf(whatever(val))

    def testdrop(self):
        self.failIf(whatever(val))

def main():
    unittest.main()

if __name__ == '__main__':
    main()
