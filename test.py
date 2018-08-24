from timer import func_timer

@func_timer
def test():
    import time
    time.sleep(3)

test()
