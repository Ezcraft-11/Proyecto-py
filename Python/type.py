
# texto (String)
x = "Hello, world" 
print(x)
print(type(x))

# numericos (int, float, complex)
x = 20 #int
print(x)
print(type(x))

x = 20.5 #float
print(x)
print(type(x))

x = 1j #complex
print(x)
print(type(x))

#list, tuple, range
x = ["apple", "banana", "cherry"] # List
print(x)
print(type(x))

x = ("apple", "banana", "cherry") #tuple
print(x)
print(type(x))

x = range(6)
print(x)
print(type(x))
# mapeo (dict)

x = {"name" : "Eze", "age" : 14}
print(x)
print(type(x))

# Set, frozenset

x = {"apple", "banana", "cherry"} #set
print(x)
print(type(x))

x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))

# Booleano (bool)

x = True
print(x)
print(type(x))

# tipos binarios (bytes, bytearray, memoryview)
x = b"Hello" #bytes
print(x)
print(type(x))

x = bytearray(5) #bytearray
print(x)
print(type(x))

x = memoryview(bytes(5)) #memoryview
print(x)
print(type(x))

# ningun tipo (NoneType)
x = None
print(x)
print(type(x))