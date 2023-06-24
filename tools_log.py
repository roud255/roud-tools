import os
import logging


'''
日志保存路径
'''
log_path = ""
LOG_FILE = log_path
if not os.path.exists(os.path.dirname(log_path)):
    os.makedirs(os.path.dirname(log_path))



class Logger:
    def __init__(self, logger=None, level=logging.INFO):
        self.logger = logging.getLogger(logger)
        self.logger.propagate = False  # 防止终端重复打印
        self.logger.setLevel(level)
        fh = logging.FileHandler(LOG_FILE, 'a', encoding='utf-8')
        fh.setLevel(level)
        #sh = logging.StreamHandler()
        #sh.setLevel(level)
        formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        fh.setFormatter(formatter)
        #sh.setFormatter(formatter)
        self.logger.handlers.clear()
        self.logger.addHandler(fh)
        #self.logger.addHandler(sh)
        fh.close()
        #sh.close()

    def get_log(self):
        return self.logger