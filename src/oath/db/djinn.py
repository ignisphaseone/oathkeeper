import ConfigParser


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
            print 'Connecting to MySQL...'
        elif db == "sqlite":
            print 'Connecting to SQLite...'
        pass


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
