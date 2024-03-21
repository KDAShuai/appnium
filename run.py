# 导入webdriver
from appium.webdriver import Remote
from appium.webdriver.common.mobileby import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

import time

account = '13350085865'
password = 'Shuai7456'

# 初始化参数
desired_caps = {
    "platformName": "Android",  # 测试版本（IOS/Android）
    "deviceName": "7d73bc84",  # 手机设备名称，通过adb devices查看
    "appPackage": "cn.xuexi.android",  # apk包名
    "appActivity": "com.alibaba.android.rimet.biz.SplashActivity",  # apk的launcherActivity
    "noReset": True,  # 不清空数据
    "unicodeKeyboard": True,  # 使用Unicode编码方式发送字符串
    "resetKeyboard": True,  # 键盘隐藏起来
    "newCommandTimeout": "1800"
}
server = 'http://localhost:4723/wd/hub'  # 127.0.0.1:4723/wb/hub：本地地址+appium端口号；appium端口号可以改变
driver = Remote(server, desired_caps)
wait = WebDriverWait(driver, 20, 0.5)
action = ActionChains(driver)
print('启动完成')
# 尝试登录
try:
    driver.find_element(
        By.XPATH, '//android.widget.EditText[@resource-id="cn.xuexi.android:id/et_phone_input"]').send_keys('account')
    driver.find_element(
        By.XPATH, '//android.widget.EditText[@resource-id="cn.xuexi.android:id/et_phone_input"]').send_keys('password')
    driver.find_element(
        By.XPATH, '//android.widget.Button[@resource-id="cn.xuexi.android:id/btn_next"]').click()
except:
    pass
# 取消更新
try:
    driver.find_element(
        By.XPATH, '//android.widget.Button[@resource-id="android:id/button2"]').click()
except:
    pass
# 等待加载
wait.until(EC.presence_of_element_located(
    (By.XPATH, '//android.widget.TextView[@resource-id="cn.xuexi.android:id/home_bottom_tab_text" and @text="电台"]')))
# 点击电台
driver.find_element(
    By.XPATH,
    '//android.widget.TextView[@resource-id="cn.xuexi.android:id/home_bottom_tab_text" and @text="电台"]').click()
# 等待加载
print('等待1s')
time.sleep(1)
print('第一次滑动')
driver.drag_and_drop(driver.find_element(By.XPATH, '//android.widget.TextView[@text="听历史"]'),
                     driver.find_element(By.XPATH, '//android.widget.TextView[@text="听同期声"]'))
print('第二次滑动')
driver.drag_and_drop(driver.find_element(By.XPATH, '//android.widget.TextView[@text="听乡村大喇叭"]'),
                     driver.find_element(By.XPATH, '//android.widget.TextView[@text="云听"]'))
# 点击听小喇叭
driver.find_element(
    By.XPATH, '//android.widget.TextView[@text="听小喇叭"]').click()
# 等待加载
wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="成语"]')))
# 点击成语
driver.find_element(By.XPATH, '//android.widget.TextView[@text="成语"]').click()
# 等待加载
wait.until(EC.presence_of_element_located(
    (By.XPATH, '//android.view.View[@content-desc="童声朗朗之成语故事 山东学习平台 9条音频"]')))
# 点击童声朗朗之成语故事
driver.find_element(By.XPATH, '//android.view.View[@content-desc="童声朗朗之成语故事 山东学习平台 9条音频"]').click()
# 等待加载
wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="全部播放"]')))
# 点击全部播放
driver.find_element(By.XPATH, '//android.widget.TextView[@text="全部播放"]').click()
# 发送三次返回键
driver.keyevent(4)
time.sleep(1)
driver.keyevent(4)
time.sleep(1)
driver.keyevent(4)


# 点击学习
driver.tap([(540, 1870)], 100)
# 等待加载
time.sleep(1)
# 点击要闻
print('要闻')
driver.tap([(180, 189)], 100)
time.sleep(3)
# 点击第一条
driver.tap([(540, 415)], 200)
time.sleep(15)
driver.swipe(540, 1200, 540, 800)
time.sleep(45)
driver.tap([(56, 98)], 200)
time.sleep(1)
# 点击第二条
driver.tap([(540, 900)], 100)
time.sleep(15)
driver.swipe(540, 1200, 540, 800)
time.sleep(45)
driver.tap([(56, 98)], 200)
time.sleep(1)
# 点击思想
print('思想')
driver.tap([(292, 189)], 100)
time.sleep(3)
# 点击第一条
driver.tap([(540, 415)], 100)
time.sleep(15)
driver.swipe(540, 1200, 540, 800)
time.sleep(45)
driver.tap([(56, 98)], 200)
time.sleep(1)
# 点击第二条
driver.tap([(540, 900)], 100)
time.sleep(15)
driver.swipe(540, 1200, 540, 800)
time.sleep(45)
driver.tap([(56, 98)], 200)
time.sleep(1)
# 点击主题教育
print('主题教育')
driver.tap([(436, 189)], 100)
time.sleep(3)
# 点击第一条
driver.tap([(540, 415)], 100)
time.sleep(15)
driver.swipe(540, 1200, 540, 800)
time.sleep(45)
driver.tap([(56, 98)], 200)
time.sleep(1)
# 点击第二条
driver.tap([(540, 900)], 100)
time.sleep(15)
driver.swipe(540, 1200, 540, 800)
time.sleep(45)
driver.tap([(56, 98)], 200)
time.sleep(1)
# 点击综合
print('综合')
driver.tap([(804, 189)], 100)
time.sleep(3)
# 点击第一条
driver.tap([(540, 415)], 100)
time.sleep(15)
driver.swipe(540, 1200, 540, 800)
time.sleep(45)
driver.tap([(56, 98)], 200)
time.sleep(1)
# 点击第二条
driver.tap([(540, 900)], 100)
time.sleep(15)
driver.swipe(540, 1200, 540, 800)
time.sleep(45)
driver.tap([(56, 98)], 200)
time.sleep(1)
# 点击县级融媒
print('县级融媒')
driver.tap([(684, 189)], 100)
time.sleep(3)
# 点击第一条
driver.tap([(540, 415)], 100)
time.sleep(15)
driver.swipe(540, 1200, 540, 800)
time.sleep(45)
driver.tap([(56, 98)], 200)
time.sleep(1)
# 点击第二条
driver.tap([(540, 900)], 100)
time.sleep(15)
driver.swipe(540, 1200, 540, 800)
time.sleep(45)
driver.tap([(56, 98)], 200)
time.sleep(1)

# # 点击积分
# print('积分')
# driver.find_element(By.XPATH,
#                     '//android.widget.LinearLayout[@resource-id="cn.xuexi.android:id/ll_comm_head_score"]').click()
# time.sleep(2)
# # 向上滑动
# driver.drag_and_drop(driver.find_element(By.XPATH, '//android.view.View[@text="我要视听学习"]'),
#                      driver.find_element(By.XPATH, '//android.view.View[@text="强国城兑福利"]'))
# driver.find_element(By.XPATH, '//android.view.View[@text="去看看"]').click()
#
# # 挑战答题
# try:
#     tiaozhandati = driver.find_element(By.XPATH, '//android.view.View[@text="挑战答题"]')
# except:
#     pass

driver.quit()
