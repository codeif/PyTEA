# -*- coding: utf-8 -*-
"""pytest test.py"""
import os
import binascii
from pytea import TEA


def test():
    key = os.urandom(16)
    print('key is: ' + str(key))
    content = u'Hello, 你好'
    tea = TEA(key)
    e = tea.encrypt(content.encode('utf-8'))
    print('encrypt hex:' + str(binascii.b2a_hex(e)))
    d = tea.decrypt(e)
    print('decrypt:' + d.decode('utf-8'))


if __name__ == '__main__':
    test()
