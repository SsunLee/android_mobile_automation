import unittest
import os
from unittest import suite
from appium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from android_course_test import AndroidCourseTest



class androidLectureClass(unittest.TestCase):
    
    def setUp(self):
        cmd = 'adb shell su 0 setprop gsm.sim.operator.iso-country kr'
        os.popen(cmd)
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                "platformName": "Android",
                "appium:platformVersion": "11.0",
                "appium:deviceName": "Android Emulator",
                "appium:app": "Users/riiid/Downloads/27688948.apk",
                "appium:automationName": "Appium",
                "appium:newCommandTimeout": "1000",
                "appium:appPackage": "co.riiid.vida",
                "appium:appActivity": "co.riiid.vida.ui.splash.SplashActivity"
            })

    def test_method(self):
        driver = self.driver 
        driver.implicitly_wait(30)

        AndroidCourseTest.email_login(self)

        selectBtnID = 'co.riiid.vida:id/fragment_self'
        selectBtn = driver.find_element(By.ID, selectBtnID)
        selectBtn.click()
        sleep(1)
        
        # check if exist bottomSheet 
        self.isPoupExist()

        # go into some lecture
        firstCell = '//android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout'
        driver.find_element(By.XPATH,firstCell ).click()
        print("강의 선택")
        sleep(0.8)

        # go into some lecture at top
        lectureEnterXpath = '//android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]'
        lectureCell = driver.find_element(By.XPATH, lectureEnterXpath)
        lectureCell.click()
        print(f"세부강의 선택 : {lectureCell.text}")
        sleep(3)

        yutubeBtnID = 'movie_player'
        if self.isShown(yutubeBtnID, By.ID):
            # iframe
            driver.find_element(By.ID, yutubeBtnID).click()
            sleep(5)
            
            

            
        








    def isPoupExist(self):
        print("entered isPopupExist")
        driver = self.driver
        testBtnClass = 'android.widget.TextView'
        try: 
            if self.isShown(testBtnClass, By.CLASS_NAME):                    
                popupBtn = driver.find_elements(By.CLASS_NAME, testBtnClass)[2]
                print(popupBtn.text)
                popupBtn.click()
                print("팝업 닫음")
        except Exception as e:
            print("팝업 없음")


    def isShown(self, selector, byType=By.XPATH):
        # 어떠한 Element 들이 다 보여진 상태를 체크하는 함수
        if self.driver.find_element(byType, selector).is_displayed():
            return True
        else:
            return False

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(androidLectureClass)
    unittest.TextTestRunner(verbosity=2).run(suite)