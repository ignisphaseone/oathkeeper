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
        curr.execute("ANALYZE sqlite_master")
        self.db.commit()
        self.db.close()

    def get_guardian(self):
        pass

    def get_warden(self):
        pass

    def get_sentry(self):
        pass

    def save_guardian(self):
        pass

    def save_warden(self):
        pass

    def save_sentry(self):
        pass
