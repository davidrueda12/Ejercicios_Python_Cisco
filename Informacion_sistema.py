from platform import platform, machine, processor, system, version, python_implementation, python_version_tuple

print(platform(aliased = False, terse = False))
print(machine())
print(processor())
print(system())
print(version())
print(python_implementation())
for atr in python_version_tuple():
    print(atr)