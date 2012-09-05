'''
Created on Sep 5, 2012

@author: ApigeeCorporation
'''
import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.secret = "12345678901234567890".encode('ascii')
        self.seq = range(10)
        self.tests = [
            "775224",
            "287082",
            "359152",
            "969429",
            "338314",
            "254676",
            "287922",
            "162583",
            "399871",
            "520489",
            ]
        pass

    def test_oath_trunc(self):
        print self.seq
        for i in self.seq:
            self.assertEquals("123456", self.tests[i], "Hashes are not equal.")
            pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
