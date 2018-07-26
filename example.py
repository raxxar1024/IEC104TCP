from iec104client import iec104_tcp_client
from iec104_tcp_packets import plist

server_ip = '123.1.1.99'
client = iec104_tcp_client(server_ip)
for p in plist:
    print(client.sendOne(p))
