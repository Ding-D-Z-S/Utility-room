import os
a=input("请输入网址")

print(a)

while True: 
  cmd = "ping www.baidu.com"

  res = os.popen(cmd)
  output_str = res.read()   # 获得输出字符串
  print(output_str)
  print(a)