from lib2to3.pgen2 import driver
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
from scriptXpath import scXpath


class androidLectureClass(unittest.TestCase):
    
    def setUp(self):
        cmd = 'adb shell su 0 setprop gsm.sim.operator.iso-country kr'
        os.popen(cmd)
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities=scXpath.device_cap)

    def test_method(self):
        driver = self.driver 
        driver.implicitly_wait(30)

        AndroidCourseTest.email_login(self)

        # if check the bottom sheet 
        blChk = AndroidCourseTest.isBottomSheetExist(self)
        if blChk == True:
            #닫는다.
            btnClose = driver.find_element(By.ID,'co.riiid.vida.staging:id/btn_close')
            btnClose.click()

        AndroidCourseTest.isPoupExist(self)


        selectBtnXpath = '//android.widget.FrameLayout[@content-desc="선택 학습"]'
        selectBtn = driver.find_element(By.XPATH, selectBtnXpath)
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
        #print(f"세부강의 선택 : {lectureCell.text}")
        sleep(3)

        self.watchingLecture(3,8)

        
        sleep(10)
        

            
    def watchingLecture(self,duration, cnt):
        endCnt = 0
        driver = self.driver
        for i in range(0,cnt):      
            endCnt += 1
            print(f'총 {cnt}회 중 {endCnt}번째')      
            yutubeXpath = '//android.view.View/android.view.View[4]/android.widget.Button'
            isPlaybtnExist = driver.find_element(By.XPATH, yutubeXpath).is_displayed()
            if isPlaybtnExist:
                driver.find_element(By.XPATH, yutubeXpath).click()
                print("재생 버튼 클릭")
                sleep(duration)
                if endCnt==cnt:
                    specificXpath = "//android.widget.Button[contains(@text,'학습 종료하기')]"
                    EndButton = driver.find_element(By.XPATH, specificXpath)
                    EndButton.click()
                    print(f"{i}회 마지막 돌입 학습 종료하기")
                    sleep(3)
                else:
                    nextLectureXpath = "//android.widget.Button[contains(@text, '다음 강의')]"
                    nextLectureBtn = driver.find_element(By.XPATH, nextLectureXpath)
                    nextLectureBtn.click()
                    print(f"{i}회차 다음 강의 시청하기 클릭")



        


            

            
        








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