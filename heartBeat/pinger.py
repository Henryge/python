import os

p = os.popen("ping www.baaaidasdfu.com")
x = p.read()
p.close()
if x.count("timeout"):
	print("ping error")
else:
	print("ping ok")