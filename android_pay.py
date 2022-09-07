
import unittest
import unittest
import os
from unittest import suite
from appium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

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
                "appium:app": "Users/riiid/Downloads/27688948.apk",
                "appium:automationName": "Appium",
                "appium:newCommandTimeout": "1000",
                "appium:appPackage": "co.riiid.vida",
                "appium:appActivity": "co.riiid.vida.ui.splash.SplashActivity"
            })

    def test_method(self):
        pass

    def tearDown(self):
        self.driver.quit()