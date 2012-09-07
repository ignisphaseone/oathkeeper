'''
Created on Sep 5, 2012

@author: ApigeeCorporation
'''
import binascii
import hashlib
import hmac
from oath import core


class guard(core.keeper):
    def __init__(self):
        pass


def cx_itoa(i):
    ox = hex(long(i))[2:-1]
    ox = '0' * (16 - len(ox)) + ox
    ob = binascii.unhexlify(ox)
    return ob


def keygen(key, i, digestmod=hashlib.sha1):
    h = hmac.new(key, cx_itoa(i), digestmod)
    s = h.digest()
    offset = stoa(s[19]) & 0xf
    bin_code = (((stoa(s[offset]) & 0x7f) << 24)
        | ((stoa(s[offset + 1]) & 0xff) << 16)
        | ((stoa(s[offset + 2]) & 0xff) << 8)
        | ((stoa(s[offset + 3]) & 0xff))
    )
    return "{:0>6}".format(bin_code % 1000000)


def stoa(s):
    return int(s.encode('hex'), 16)
