from selenium import webdriver
import time
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()



'''
selenium工具类，用于爬虫和自动化测试
'''

driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})

'''
手机号
'''
number = ""

def demo():
    # 获取谷歌浏览器driver对象
    driver = webdriver.Chrome()
    # 打开百度首页
    driver.get("https://baidu.com")
    # 页面全屏
    driver.maximize_window()
    # 通过xpath方式获取输入框并输入selenium
    driver.find_element_by_xpath('//*[@id="kw"]').send_keys("selenium")
    # 通过xpath方式获取搜索按钮并点击
    driver.find_element_by_xpath('//*[@id="su"]').click()
    # 休息5秒
    time.sleep(5)
    # 关闭
    driver.close()

# 轨迹函数：将距离细分为几个小的数组段，返回数组。目的是为了模拟滑动痕迹
# 参数distance：要移动的距离
def get_track(distance):
    tracks = []
    current = 0
    mid = distance * (0.7)
    t = 0.2
    v = 0

    while (current < distance):
        if (current < mid):
            a = 3
        else:
            a = -2
        v0 = v
        v = v0 + a * t
        moves = v0 * t + (0.5) * a * t ** 2
        current += moves
        tracks.append(round(moves))
    return tracks


# 移动函数1，主要是模拟人为移动，先快后慢。执行效率低，但可以避开某些网站的安全识别
# 参1：要移动的距离
# 参2：移动小滑块的xpth路径
def move_to(distance, moveboxPath):
    print("程序开始...")
    ts = get_track(distance)
    print("获取轨迹数组成功")
    movebox = driver.find_element_by_xpath(moveboxPath)
    print("获取滑块成功")
    ActionChains(driver).click_and_hold(movebox).perform()
    for a in ts:
        ActionChains(driver).move_by_offset(xoffset=a, yoffset=0).perform()
    time.sleep(0.5)
    ActionChains(driver).release().perform()


# 移动函数1，直接移动距离，匀速但非常快。执行效率高，但容易被网站的识别为机器人
# 参1：要移动的距离
# 参2：移动小滑块的xpth路径
def move_to2(distance, moveboxPath):
    print("程序开始...")
    print("获取轨迹数组成功")
    movebox = driver.find_element_by_xpath(moveboxPath)
    print("获取滑块成功")
    ActionChains(driver).click_and_hold(movebox).perform()
    ActionChains(driver).move_by_offset(xoffset=distance, yoffset=0).perform()
    ActionChains(driver).release().perform()


'''
模拟滑动滑块验证后点击发送验证码
'''


# 向右滑动验证
# 滑动后点击发送验证码就可以发送
def driver_goRight(url, phoneInput, distance, moveboxPath, sendClick):
    driver.get(url)
    driver.maximize_window()
    driver.find_element_by_xpath(phoneInput).send_keys(number)
    move_to(distance, moveboxPath)
    time.sleep(0.5)
    driver.find_element_by_xpath(sendClick).click()
    time.sleep(5)
    print("点击发送成功")
    driver.close()


# 向右滑动验证
# 点击发送验证码才跳出滑框
def driver_goRight2(url, phoneInput, distance, moveboxPath, sendClick, framepath):
    driver.get(url)
    driver.maximize_window()
    driver.find_element_by_xpath(phoneInput).send_keys(number)
    driver.find_element_by_xpath(sendClick).click()
    time.sleep(0.5)
    driver.switch_to.frame(framepath)
    move_to(distance, moveboxPath)
    time.sleep(0.5)

    print("点击发送成功")
    driver.close()


# 点击验证
def driver_goClick(url, phoneInput, clickBox, sendClick):
    driver.get(url)
    driver.maximize_window()
    driver.find_element_by_xpath(phoneInput).send_keys(number)
    driver.find_element_by_xpath(clickBox).click()
    time.sleep(5)
    driver.find_element_by_xpath(sendClick).click()
    time.sleep(3)
    print("点击发送成功")
    driver.close()
