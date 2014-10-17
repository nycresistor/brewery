#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Database toolkit tests
   Tests the initialization
   Creation
   Population
   Destruction
   And Changes to the database as a common
   db method set.
"""

import unittest


from common import db


# Here's our "unit".
def InitDB():
    return 0

# Here's our "unit tests".
class InitDBTests(unittest.TestCase):

    def testcreate(self):
        self.failUnless(db.mysql_init())

    def testinsert(self):
        self.failUnless(db.mysql_insert(arg))

    def testdelete(self):
        #self.failIf(db.mysql_delete(arg))
        self.failUnless(db.mysql_delete(arg))

    def testdrop(self):
        self.failUnless(db.mysql_drop(table))

def main():
    unittest.main()

if __name__ == '__main__':
    main()
