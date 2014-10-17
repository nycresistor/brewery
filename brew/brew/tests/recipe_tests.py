#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
recipe method tests
   creation
   modifcation
   deletion
"""

import unittest


from common import db


# Here's our "unit".
def InitRecipe():
    return 0

# Here's our "unit tests".
class RecipeTests(unittest.TestCase):

    def recipecreate(self):
        self.failUnless(db.mysql_init())

    def recipemod(self):
        self.failUnless(db.mysql_insert(arg))

    def recipedelete(self):
        #self.failIf(db.mysql_delete(arg))
        self.failUnless(db.mysql_delete(arg))

def main():
    unittest.main()

if __name__ == '__main__':
    main()
