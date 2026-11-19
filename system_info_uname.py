import os
info = os.uname()

print(f"System name (sysname) : {info.sysname}")
print(f"Node name (nodename) : {info.nodename}")
print(f"Kernel release  : {info.release}")
print(f"Kernel version : {info.version}")
print(f"Machine architecture : {info.machine}")
if hasattr(info, "processor"):
	print(f"Processor      : {info.processor}")
          
