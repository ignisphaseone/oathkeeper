'''
Created on Sep 5, 2012

@author: ApigeeCorporation
'''
import unittest
from oath.hotp import keygen, guardian
import hashlib
from oath.db.djinn import djinn


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
        '''
            Check test.db for SQLite here. Create it if not available.
            Do not check for MySQL info here; that is an actual part of the
            MySQL testing.
        '''

    def test_oath_trunc(self):
        self.results = []
        for i in self.seq:
            self.results.append(keygen(self.secret, i, hashlib.sha1))
        for i in range(self.results.__len__()):
            print self.results[i], self.tests[i]
            self.assertEquals(self.results[i], self.tests[i],
                              "Hashes are not equal.")

    def test_basic_init(self):
        myguard = guardian(self.secret, 0)
        self.assertEqual(myguard.secret, self.secret,
                         "myguard secrets do not match.")
        myguard = guardian(self.secret, 0, form="dec7")
        self.assertEqual(myguard.secret, self.secret,
                         "myguard secrets do not match.")
        self.assertEqual(myguard.form, "dec7",
                         "myguard forms do not match.")

    def test_djinn(self):
        d = djinn('settings.cfg')
        print d.config.get('database', 'user'), "root"
        self.assertEqual(d.config.get('database', 'user'), "root",
                         "'settings.cfg username does not match 'root'")
        print d.config.get('database', 'password'), "admin"
        self.assertEqual(d.config.get('database', 'password'), "admin",
                         "'settings.cfg password does not match 'admin'")
        if d.config.get('database', 'db') == "sqlite":
            print "Connecting to SQLite..."
        elif d.config.get('database', 'db') == "mysql":
            print "Connecting to MySQL..."
        else:
            self.assertRaises(Exception, d.db_connect())
        d.db_connect()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
