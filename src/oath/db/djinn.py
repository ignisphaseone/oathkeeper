import ConfigParser
import sqlite3
from sqlite3 import OperationalError
from oath.hotp import guardian
import hmac
import hashlib


class djinn():
    def __init__(self, filename):
        self.config = ConfigParser.SafeConfigParser()
        if filename is None:
            self.config.readfp(open('default_filename'))
        else:
            self.config.readfp(open(filename))
        pass

    def db_connect(self):
        db = self.config.get('database', 'db')
        if db == "mysql":
            self.__mysql()
        elif db == "sqlite":
            self.__sqlite()
        else:
            raise Exception
        pass

    def __mysql(self):
        pass

    def __sqlite(self):
        fname = self.config.get('database', 'db.name')
        self.db = sqlite3.connect(fname)
        self.db.row_factory = sqlite3.Row

    def clear_db(self):
        curr = self.db.cursor()
        curr.execute("""
            DELETE FROM user WHERE uname
        """)
        self.db.commit()

    def __close_db(self):
        self.db.close()

    def get_keeper(self, uname, passwd):
        curr = self.db.cursor()
        curr.execute("""
            SELECT * FROM user WHERE uname = (?)
        """, uname)
        pass

    def put_keeper(self, uname, passwd, type, secret, form):
        curr = self.db.cursor()
        hspasswd = hmac.new(secret, passwd, hashlib.sha1)
        curr.execute("""
            INSERT INTO user VALUES (?,?,?,?,?)
        """, uname, hspasswd, type, secret, form)
