from oath import core
import time


class sentry(core.keeper):
    def __init__(self, secret, form="dec6"):
        core.keeper.__init__(self, secret, form)
        self.offset = 0
        pass

    def sync(self):
        return int(time.time())
