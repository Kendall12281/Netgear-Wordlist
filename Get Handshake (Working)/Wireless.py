import subprocess as s
txt=s.check_output(["netsh","wlan","disconnect"])
text=s.check_output(["netsh","wlan","show","networks"])
print(text.decode())



