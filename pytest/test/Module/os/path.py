#! encoding:utf-8
import os
# 是后者
print('Is the abs path of execute file or running directory')
path = os.getcwd()
print(path)

from pathlib import Path

P = Path(__file__).resolve()
print('current path', P)

print('print parent directory')
print('parent path',P.parent)
print('parent path',P.parent.parent)
