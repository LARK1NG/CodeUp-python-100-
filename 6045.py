# 정수 3개를 입력받아 합과 평균을 출력해보자.

from distutils.spawn import spawn
from posixpath import split


a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
print(a + b + c, '%.2f' %((a + b + c) / 3))

a, b, c = input().split()
a=int(a)
b=int(b)
c=int(c)
hap=a+b+c
avg=hap/3
print(hap, format(avg, ".2f"))