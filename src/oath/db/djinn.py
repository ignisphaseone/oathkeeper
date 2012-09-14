import ConfigParser
import sqlite3
from sqlite3 import OperationalError


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
        curr = self.db.cursor()
        try:
            curr.execute("CREATE TABLE user (uname, type, pass, secret, counter)")
        except OperationalError:
            curr.execute("""DELETE FROM user WHERE uname is 'ignis'""")
            curr.execute("""INSERT INTO user VALUES
                ('ignis','guardian','secret','12345678901234567890', 0)""")
            for row in curr.execute("SELECT * FROM user"):
                print row
        self.db.commit()
        self.db.close()

    def get_guardian(self):
        pass

    def get_warden(self):
        pass

    def get_sentry(self):
        pass

    def save_guardian(self, g):
        pass

    def save_warden(self, w):
        pass

    def save_sentry(self, s):
        pass
