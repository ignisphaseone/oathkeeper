'''
Created on Aug 28, 2012

@author: ignisphaseone
'''
import hmac
import hashlib
from twisted.python.randbytes import secureRandom
import time
import struct


secret = bytes(secureRandom(20))
print "{:->16}".format("secret bytes:"), secret
print "{:->16}".format("secret int:"), int(secret.encode('hex'), 16)
print "{:->16}".format("secret bin:"), "{:0>160}".format(str(bin(int(secret.encode('hex'), 16))).replace("0b", ""))
mytime = int(time.time())
print "{:->16}".format("time int:"), mytime
datatime = struct.pack('>I', mytime)
print "{:->16}".format("time bytes:"), datatime
print "{:->16}".format("time int bin:"), "{:0>32}".format(str(bin(mytime)).replace("0b", ""))
print "{:->16}".format("time bytes bin:"), "{:0>32}".format(str(bin(int(datatime.encode('hex'), 16))).replace("0b", ""))
myhash = hmac.new(secret)
myhash.update(datatime)
print myhash.hexdigest()
