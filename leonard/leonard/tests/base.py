#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
"""

import sys
import unittest

sys.path.append('../../')


# Here's our "unit".
def LeonardBase():
    return 0

# Here's our "unit tests".
class LeonardBaseTests(unittest.TestCase):

    def testcreate(self):
        self.assertIsNone(lolwhat?)


def main():
    unittest.main()

if __name__ == '__main__':
    main()