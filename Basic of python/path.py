print("Printing Path Of my system")
import sys
print(sys.path)

print("Printing path of current working directory")
import os
path=os.getcwd()
print (path)

print("Appending the current path directory in system path")
sys.path.append(path)
print (sys.path)
