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
from scriptXpath import scXpath


class androidTestPrepClass(unittest.TestCase):

    def setUp(self) -> None:
        cmd = 'adb shell su 0 setprop gsm.sim.operator.iso-country kr'
        os.popen(cmd)
        cap = scXpath.getPath('riiid', '27706198')
        print(cap)
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities=cap)
        
    def test_method1(self):
        driver = self.driver
        AndroidCourseTest.email_login(self)
        sleep(2.2)

        blChk = AndroidCourseTest.isBottomSheetExist(self)
        if blChk:
            btnClose = driver.find_element(By.ID, 'co.riiid.vida.staging:id/btn_close')
            btnClose.click()

        sleep(3)

        selfLearningBtnScript = '//android.widget.FrameLayout[@content-desc="선택 학습"]'
        selfLearningBtn = driver.find_element(By.XPATH, selfLearningBtnScript)
        selfLearningBtn.click()
        sleep(3)

        # check if popup 
        AndroidCourseTest.isPoupExist(self)

        # 기초 첫 번째
        testScript = '//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]'
        #testScript = "android.widget.TextView[@text, '문제']"
        testBtn = driver.find_element(By.XPATH, testScript)
        testBtn.clcik()



        print('test')
        

    def tearDown(self) -> None:
        self.driver.quit()






if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(androidTestPrepClass)
    unittest.TextTestRunner(verbosity=2).run(suite)