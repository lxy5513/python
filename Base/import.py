import sys 

print(sys.path)

# import current path
import rename_img as img 
from rename_img import ImageRename as Img
b = Img()
a = img.ImageRename()
print(a, b)

# import parent path 
from ..Wraps import timeout 
