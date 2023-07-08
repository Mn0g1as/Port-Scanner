#Made by Mn0g1as
# Have fun :)

import socket
ip =  'ip'
#port 9000
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  for port in range(100, 65500):
    try:
      s.connect(ip, port)
      print(f' port {port} is open! ')

except:

print(f' port {port} is not open! ')


