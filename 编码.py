﻿'''
某种编码由六位二进制码组成，前三位表示方向，后三位表示距离。
输入一组六位二进制码,将编码翻译成方向和距离，距离值为每组编码后三位二进制码转换为十进制数的值。
'''


s =input("输入一组六位二进制：")
i = 0
c =s[i:i+3]
if c == "000":
    d = "东"
elif c == "001":
    d = "东南"
elif c == "010":
    d = "南"
elif c == "011":
    d = "西南"
elif c == "100":
    d = "西"
elif c == "101":
    d = "西北"
elif c == "110":
    d = "北"
else:
    d = "东北"
b1 = int(s[i + 3])
b2 = int(s[i + 4])
b3 = int(s[i + 5])
v=b1*2**2+b2*2**1+b3*2**0          
print( d +" " + str(v))      





