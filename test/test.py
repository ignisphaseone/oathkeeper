'''
Created on Sep 5, 2012

@author: ApigeeCorporation
'''
import unittest
from oath.hotp import scribe
import hashlib


class Test(unittest.TestCase):
    def setUp(self):
        self.secret = "12345678901234567890".encode('ascii')
        self.seq = range(10)
        self.tests = [
            "755224",
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
        self.results = []
        for i in self.seq:
            self.results.append(scribe(self.secret, i, hashlib.sha1))
        for i in range(self.results.__len__()):
            print self.results[i], self.tests[i]
            self.assertEquals(self.results[i], self.tests[i],
                              "Hashes are not equal.")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
