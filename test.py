#
# Copyright(C) 2015. Sungho Park
# This module is distributed under Apache 2.0 license.
#

__author__ = 'Sungho Park'

import unittest
import pau

class VersatileDictTest(unittest.TestCase):
    def setUp(self):
        self.dict_data1 = {"KEY1": "DATA1", "KEY2": 1}
        self.books=[]
        self.books.append({"Title": "The python programming", "Author": "Sungho Park"})

        self.dict_data2 = {""}

    def test_basic(self):
        test = pau.VersatileDict()
        test.add("dict/test", self.dict_data1)
        print("Data", test)

if __name__ == '__main__':
    unittest.main()
