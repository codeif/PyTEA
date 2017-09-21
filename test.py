# -*- coding: utf-8 -*-
"""pytest test.py"""
import os
from pytea import TEA


def test():
    key = os.urandom(16)
    print('key is', key)
    content = 'Hello, 你好'
    tea = TEA(key)
    e = tea.encrypt(content.encode())
    print('encrypt hex:', e.hex())
    d = tea.decrypt(e)
    print('decrypt:', d.decode())


if __name__ == '__main__':
    test()
