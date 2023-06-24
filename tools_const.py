import random
import time

from common_const import headers_only_useragent_chrome, headers_only_useragent_firefox, headers_only_useragent_edg, \
    user_agent_chrome, user_agent_firefox, user_agent_edg


def get_headers_only_user_agent():
    headers = ""
    try:
        # =0 =2
        i = random.randint(0, 3)
        if i == 0:
            headers = headers_only_useragent_chrome
        elif i == 1:
            headers = headers_only_useragent_firefox
        elif i == 2:
            headers = headers_only_useragent_edg
        return headers
    except:
        return headers

def get_only_user_agent():
    ua = ""
    try:
        # =0 =2
        i = random.randint(0, 3)
        if i == 0:
            headers = user_agent_chrome
        elif i == 1:
            headers = user_agent_firefox
        elif i == 2:
            headers = user_agent_edg
        return headers
    except:
        return ua


def get_timetemp():
    return str(int(time.time() * 1000))