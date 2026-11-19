import os
import platform
import socket

print(f"socket.gethostname():", socket.gethostname())

print(f"os.uname().nodename:", os.uname().nodename)
print(f"platform.node() :", platform.node())

print(f"socket.getfqdn() :", socket.getfqdn())


