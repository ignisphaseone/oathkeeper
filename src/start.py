'''
Created on Aug 28, 2012

@author: ignisphaseone
'''
import hmac
from twisted.python.randbytes import secureRandom
import hashlib
import time
import struct


digits = 6
mod_digits = 10
for i in range(1, digits):
    mod_digits = mod_digits * 10


def oath_trunc(s):
    myoff = ""
    for c in range(16, 20):
        myoff += s[int(s[c].encode('hex'), 16) % 16]
    offset = stoa(s[19]) & 0xf
    print s
    print myoff, offset
    bin_code = (((stoa(s[offset]) & 0x7f) << 24)
        | ((stoa(s[offset + 1]) & 0xff) << 16)
        | ((stoa(s[offset + 2]) & 0xff) << 8)
        | ((stoa(s[offset + 3]) & 0xff))
    )
    return "{:0>6}".format(bin_code % mod_digits)


def stoa(s):
    return int(s.encode('hex'), 16)

secret = bytes(secureRandom(20))
print ("{:->16}".format("secret bytes:"), unicode(secret))
print ("{:->16}".format("secret int:"), int(secret.encode('hex'), 16))
print ("{:->16}".format("secret bin:"),
       "{:0>160}".format(str(bin(int(secret.encode('hex'), 16)))
                         .replace("0b", "")))
mytime = int(time.time())
print ("{:->16}".format("time int:"), mytime)
datatime = struct.pack('>I', mytime)
print ("{:->16}".format("time bytes:"), unicode(datatime))
print ("{:->16}".format("time int bin:"),
       "{:0>32}".format(str(bin(mytime)).replace("0b", "")))
print ("{:->16}".format("time bytes bin:"),
       "{:0>32}".format(str(bin(int(datatime.encode('hex'), 16)))
                        .replace("0b", "")))
myhash = hmac.new(secret, datatime, hashlib.sha1)
print myhash.hexdigest()
print int(myhash.hexdigest(), 16)
print bin(int(myhash.hexdigest(), 16)).replace("0b", "")
print int(bin(int(myhash.hexdigest(), 16)).replace("0b", ""), 2)
print myhash.digest()
print oath_trunc(myhash.digest())
for i in range(1, 60):
    h = hmac.new(secret, struct.pack('>I', int(time.time())), hashlib.sha1)
    print oath_trunc(h.digest())
    time.sleep(1)
