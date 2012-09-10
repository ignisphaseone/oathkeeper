import ConfigParser
import sqlite3


class djinn():
    def __init__(self, filename):
        self.config = ConfigParser.SafeConfigParser()
        if filename is None:
            self.config.readfp(open('default_filename'))
        else:
            self.config.readfp(open(filename))
        pass

    def db_connect(self):
        print self.config.get('database', 'user')
        print self.config.get('database', 'password')
        db = self.config.get('database', 'db')
        print db
        if db == "mysql":
            self.__mysql()
        elif db == "sqlite":
            self.__sqlite()
        pass

    def __mysql(self):
        print 'Connecting to MySQL...'

    def __sqlite(self):
        print 'Connecting to SQLite...'
        fname = self.config.get('database', 'db.name')
        self.db = sqlite3.connect(fname)
        curr = self.db.cursor()
        curr.execute("ANALYZE sqlite_master")
        self.db.commit()
        self.db.close()


def get_guard():
    pass


def get_warden():
    pass


def get_sentry():
    pass


def save_guard():
    pass


def save_warden():
    pass


def save_sentry():
    pass
