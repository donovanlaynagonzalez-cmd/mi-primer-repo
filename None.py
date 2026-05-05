from sys import dont_write_bytecode


x = None

print(x)

print(type(x))

print(type(""))
print(type(0))
print(type(False))
print(type([]))

x = "donde"
x2 = x.upper()
print(x2)