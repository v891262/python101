#!/usr/bin/env python3
switch = {"hostname": "sw1", "ip": "10.0.1.1", "version": "1.2", "vendor": "cisco"}
## Display parts of the dictionary 
print(switch["hostname"])
print(switch["ip"])
##request a 'fake' key
#print(switch["lynx"])
print("first test = .get()")
print(switch.get("lynx"))

print("Second test = .get()")
print(switch.get("lynx", "The KEY IS IN ANOTHER CASTLE!"))

print("Third test = .get()")
print(switch.get("version"))

print("Forth test = .keys()")
print(switch.keys())

print("Fifth test = .values()")
print(switch.values())

print("Sixth test = .pop()")
switch.pop("version")
print(switch.keys())
print(switch.values())

print("Seventh test = ADD a new value")
switch["adminlogin"] = 'kar108'
print(switch.keys()) 
print(switch.values())

print("Eights Test - ADD a new value")
switch["password"] = 'qwerty'
print(switch.keys())
print(switch.values())

