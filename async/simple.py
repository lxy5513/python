import asyncio 
#  async def myfun(i):   
    #  print('start {}th'.format(i))    
    #  await asyncio.sleep(1)    
    #  print('finish {}th'.format(i))
        
#  loop = asyncio.get_event_loop()
#  myfun_list = (myfun(i) for i in range(10))
#  loop.run_until_complete(asyncio.gather(*myfun_list))


import time 
def myfun(i):
    print('Strat {}th'.format(i))
    time.sleep(1)
    print('End {}th'.format(i))

async def main():
    loop = asyncio.get_event_loop()
    futures = (
            loop.run_in_executer(
                None, myfun, i
                ) 
            for i in range(10)
            )

    for result in await asyncio.gather(*futures):
        pass


loop = asyncio.get_event_loop() 
loop.run_until_complete(main()) 

