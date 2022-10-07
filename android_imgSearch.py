

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
from pyautogui import ImageNotFoundException
import pyautogui
import cv2

class androidImgClass(unittest.TestCase):

    def setUp(self):
        cmd = 'adb shell su 0 setprop gsm.sim.operator.iso-country kr'
        os.popen(cmd=cmd)
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities=scXpath.device_cap
        )
    
    def test_img1(self):
        driver = self.driver
        driver.update_settings({"getMatchedImageResult": True})

        el = driver.find_element_by_image('/Users/riiid/Downloads/start.png')
        el.get_attribute('visual')
        el.click()
        

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(androidImgClass)
    unittest.TextTestRunner(verbosity=2).run(suite)
