#!/bin/python2

import binascii

k1 = bytearray.fromhex("30167b0eb4eef511ec82272b4b47a2d71471")
k2 = bytearray.fromhex("1319057cb23c1dcbf616876372617fff8b48")
res = bytearray(k1[i] ^ k2[i] for i in range(0, len(k1)))
print "    " + binascii.hexlify(k1)
print "xor " + binascii.hexlify(k2)
print "    ------------"
print "    " + binascii.hexlify(res)
