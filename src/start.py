'''
Created on Aug 28, 2012

@author: ignisphaseone
'''
import hmac
import hashlib
from twisted.python.randbytes import secureRandom
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
print "--size of a set string 'blah':"
s = "blah"
print s
print s.__class__
print s.__sizeof__()
print unicode(s)
print unicode(s).__class__
print unicode(s).__sizeof__()
print "--attempted binary conversions of s (into ints?)"
print s
print bin(int(s.encode('hex'), 16))
