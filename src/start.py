'''
Created on Aug 28, 2012

@author: ignisphaseone
'''
import hmac
import hashlib
from twisted.python.randbytes import secureRandom
import struct
import time

d = secureRandom(20)
print "--string representation of secure random (20 bytes):"
print d
print d.__class__
print d.__sizeof__()
i = int(d.encode('hex'), 16)
print "--long representation of secure random (20 bytes):"
print i
print bin(i)
print i.__class__
t = int(time.time())
print "--time since epoch:"
print t
print bin(t)
print t.__class__
print t.__sizeof__()
