#!/usr/local/bin/python3
"""使用了 while 来计算 1 到 100 的总和"""
n = 100
a, b = 0, 1
while b <= n:
    a = a + b
    b += 1
print('1 到 %d 之和为：%d' % (n, a))
