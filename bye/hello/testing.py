from dir0 import changepath
import os
path =  os.path.realpath(__file__)
print('path -',path)
path1 = changepath(path,1)

print(path1)
