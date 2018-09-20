# Python Log

## log level
    DEBUG < INFO < WARNING < ERROR < CRITICAL
    DEBUG: 最详细的日志信息
    INFO: 用于确定一切都是按照我们预期的那样进行工作
    WARNING: 当不期望的事情发生时记录的信息，　但程序还是能照常运行
    ERROR: 一部份功能不能照常运行

    指定一个级别后　会记录大于或等于该级别的信息

    logging.basicCoonfig(level=logging.INFO)

## variable output
    logging.warning('%s is %d years old', 'Ferry', 24)
