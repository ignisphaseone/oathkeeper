from twisted.python.randbytes import secureRandom
import hashlib
class keeper():
    def __init__(self, secret, form="dec6"):
        self.secret = secret
        self.form = form

    def sync(self):
        pass


def gen_passwd(s):
    secret = secureRandom(20)
    h = hashlib.sha1()
    h.update(secret)
    h.update(s)
    hspass = h.hexdigest()
    return secret, hspass
