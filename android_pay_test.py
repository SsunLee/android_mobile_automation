
import email
from email.policy import default
import unittest
import os
from unittest import suite
from appium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from appium.webdriver.common.touch_action import TouchAction
from android_course_test import AndroidCourseTest
import random
from selenium.webdriver.common.keys import Keys



class androidPayClass(unittest.TestCase):
   
    def setUp(self):
        cmd = 'adb shell su 0 setprop gsm.sim.operator.iso-country kr'
        os.popen(cmd)
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                "platformName": "Android",
                "appium:platformVersion": "11.0",
                "appium:deviceName": "Android Emulator",
                "appium:app": "Users/riiid/Downloads/27706198.apk",
                "appium:automationName": "Appium",
                "appium:newCommandTimeout": "1000",
                "appium:appPackage": "co.riiid.vida.staging",
                "appium:appActivity": "co.riiid.vida.ui.splash.SplashActivity"
            })

    def test_method(self):
        driver = self.driver
        AndroidCourseTest.email_login(self)
        sleep(2.2)

        # if check the bottom sheet 
        blChk = self.isBottomSheetExist()
        if blChk == True:
            #닫는다.
            btnClose = driver.find_element(By.ID,'co.riiid.vida.staging:id/btn_close')
            btnClose.click()

        AndroidCourseTest.isPoupExist(self)
        iv_cart = '//android.view.ViewGroup/android.widget.ImageView[2]'
        cartEle = driver.find_element(By.XPATH, iv_cart)
        cartEle.click()
        print("move to cart")
        sleep(3)
        driver.implicitly_wait(10)
        
        # cart page 
        iv_board = '//android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[2]/android.view.View[1]'
        boardEle = driver.find_element(By.XPATH, iv_board)
        boardEle.click()
        print("click board")
        sleep(3)

        iv_Buybtn = '//android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.Button'
        BuybtnEle = driver.find_element(By.XPATH, iv_Buybtn)
        BuybtnEle.click()
        print("click buy")
        sleep(3)

        # iv_detailBuy = '//android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.Button'
        # detailBuyEle = driver.find_element(By.XPATH, iv_detailBuy)
        # detailBuyEle.click()
        # print("click detaail click")
        # sleep(3)

        # scroll to bottom
        #self.ActionDrag()
        driver.swipe(800, 2242,798, 963, 1500)

        sleep(0.8)
        iv_NaverPay = '//android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.Button[2]'
        NaverPayEle = driver.find_element(By.XPATH, iv_NaverPay)
        NaverPayEle.click()


        # 이 부분은 못찾고 있음
        iv_lastBuy = '//android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.Button'
        lastBuyEle = driver.find_element(By.XPATH, iv_lastBuy)
        lastBuyEle.click()
        print("click detaail click")


        # naver login t_t
        emailField = driver.find_element(By.XPATH, '//android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.view.View[3]/android.view.View/android.view.View[1]/android.view.View/android.widget.EditText')
        emailField.click()
        emailtext = 'tnsqo1126'
        emailField.send_keys(emailtext)
        # for c in emailtext:  
        #     i = random.randrange(0, 10)
        #     index = i / 100
        #     sleep(index)
        #     print(index)
        #     emailField.send_keys(c)
        sleep(2)

        # password field 
        passField = driver.find_element(By.XPATH, '//android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.view.View[3]/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText')
        passField.click()
        passdata = 'zmfjrtmqaqa1@1@'
        passField.send_keys(passdata)
        sleep(0.8)        
        loginBtn = driver.find_element(By.XPATH, '//android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.widget.Button')
        loginBtn.click()

        # new browser environment
        notAdd = driver.find_element(By.XPATH, '//android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[4]/android.widget.Button[2]')
        notAdd.click()
        sleep(0.8)

        driver.swipe(800, 2242,798, 200, 1500)

        # switch NaverPay WebView 
        NaverPayWebView = driver.contexts[1]
        driver.switch_to.context(NaverPayWebView)
        

        TouchAction(driver).tap(None, 200, 620, 1).perform()

        DefaultView = driver.context[0]
        driver.switch_to.context(DefaultView)
        
        #driver.find_element(By.XPATH, '//div[@id="pageNavigation"]').click()
        driver.implicitly_wait(20)
        


        sleep(10)






    def ActionDrag(self):
        driver = self.driver
        # actions = ActionChains(driver)
        # builder = actions.w3c_actions = ActionBuilder(driver)
        # builder.add_pointer_input('touch', ":touch")
        # actions.w3c_actions.pointer_action.move_to_location(820, 2242)
        # actions.w3c_actions.pointer_action.pointer_down()
        # actions.w3c_actions.pointer_action.move_to_location(798, 963)
        # actions.w3c_actions.pointer_action.release()
        # actions.perform()
        driver.swipe(800, 2242,798, 963, 1500)

        # startPath = '//android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[2]/android.view.View[4]'
        # endPath = '//android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View[11]'
        # spEle = driver.find_element(By.XPATH, startPath)
        # ePEle = driver.find_element(By.XPATH, endPath)
        # driver.scroll(spEle, ePEle)
        



    # 나중에 분리 예정
    def isBottomSheetExist(self):
        driver = self.driver
        print("Bottom 시트가 있는지 Check ")
        blChk = driver.find_element(By.ID,'co.riiid.vida.staging:id/iv_marketing_image').is_displayed()
        if blChk:
            print("BottomSheet 존재!")
            return True
        else:
            print("BottomSheet 없음!")
            return False


    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(androidPayClass)
    unittest.TextTestRunner(verbosity=2).run(suite)