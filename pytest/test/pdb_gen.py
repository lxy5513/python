def gene(i=0):
    print('generator...')
    while True:
        i += 1
        return i 

import ipdb 
ipdb.set_trace()
print('start ...')
result = gene()
print('over')

