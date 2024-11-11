from sympy import factorint
from Cryptodome.Util.number import bytes_to_long

P = 10061
PP = 10427

Text = "Flag{XXXXXXXXXX}" # 16 bytes
loong = bytes_to_long(Text.encode())

factors = factorint(loong)
for i in factors.keys():
    for j in range(factors[i]):
        print(i%P, i%PP)
"""
output:
3 3
11 11
7561 7561
7084 1594
7534 9049
9111 795
2696 2928
"""